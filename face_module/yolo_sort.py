import os
# limit the number of cpus used by high performance libraries
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
from pathlib import Path

import warnings
warnings.filterwarnings('ignore')

import torch

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # yolov5 strongsort root directory
WEIGHTS = ROOT / 'weights'

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
if str(ROOT / 'yolov5') not in sys.path:
    sys.path.append(str(ROOT / 'yolov5'))  # add yolov5 ROOT to PATH
if str(ROOT / 'strong_sort') not in sys.path:
    sys.path.append(str(ROOT / 'strong_sort'))  # add strong_sort ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from yolov5.utils.general import scale_coords, non_max_suppression_face, xyxy2xywh_wide,xyxy2xywh,xyxy_wide2xyxy_narrow
from yolov5.utils.plots import Annotator, colors
from yolov5.utils.torch_utils import select_device
from yolov5.utils.dataloaders import LoadImages
from yolov5.models.experimental import attempt_load
import cv2
import shutil
from moviepy.editor import AudioFileClip,VideoClip
import numpy as np
import math

# 상관관계, 카이제곱 검정, 교차검정, 비타차야 거리
VALIDMETHOD=[cv2.HISTCMP_CORREL,cv2.HISTCMP_CHISQR,cv2.HISTCMP_INTERSECT,cv2.HISTCMP_BHATTACHARYYA]

from strong_sort.strong_sort import StrongSORT
class FaceTracker:
    def __init__(
        self,
        device: str = "cpu",
        image_size: int = 640,
        view_img: bool = True,
        augment: bool = False,
        video_path: str=''
    ):
        self.model_path = WEIGHTS / 'yolov5s-face.pt'
        self.device = select_device(device)
        self.load_model()
        self.prediction_list = None
        self.image_size = image_size
        self.config_path = WEIGHTS / 'osnet_ain_x1_0_msmt17.pt'
        self.view_img = view_img
        self.augment = augment
        self.video_path=video_path
        self.dataTable=None
        self.video_frames=None
        self.fps=30
        self.video_len=0
        
    def load_model(self):
        self.model = attempt_load(self.model_path, device=self.device)
    
    def tracking(self,confence,sort_option,thread):
        self.model.conf=confence
        dataset = LoadImages(self.video_path, self.image_size)  
        strongsort_list = []        
        strongsort_list.append(
            StrongSORT(
                model_weights= self.config_path,
                device=self.device,
                max_dist=sort_option['MAX_DIST'],
                max_iou_distance=sort_option['MAX_IOU_DISTANCE'],
                max_age=sort_option['MAX_AGE'],
                n_init=sort_option['N_INIT'],
                nn_budget=sort_option['NN_BUDGET'],
                mc_lambda=sort_option['MC_LAMBDA'],
                ema_alpha=sort_option['EMA_ALPHA'],
            )
        )
        self.dataTable=[]

        outputs = [None] 
        previous_frame,current_frame=[None],[None]  
        max_conf=dict() # to id
        for fn,(path, im, im0s, vid_cap, s) in enumerate(dataset):
            if not thread.power:
                break
            imBox=im0s.copy()
            im = torch.from_numpy(im).to(self.device)
            im = im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim

            inf_out,_= self.model(im,augment=self.augment) 
            pred = non_max_suppression_face(inf_out,conf_thres=self.model.conf)#, conf_thres=self.model.conf, iou_thres=self.model.iou, classes=self.model.classes)
            
            for i, det in enumerate(pred):
                annotator = Annotator(imBox, line_width=2, example=str(self.model.names))
                current_frame[i]=im0s.copy()

                if sort_option['ECC']:  # camera motion compensation
                    strongsort_list[i].tracker.camera_update(previous_frame[i],current_frame[i])
                det.to(self.device)
                if len(det):
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0s.shape).round()
                    xywhs_wide=xyxy2xywh_wide(det[:,:4]).cpu().detach()
                    confs = det[:, 4].cpu().detach()
                    clss = det[:, 15].cpu().detach()
                    outputs[i] = strongsort_list[i].update(xywhs_wide, confs, clss, im0s)
                    row=dict()
                    if len(outputs[i]) > 0:
                        for j, (output, conf) in enumerate(zip(outputs[i], confs)):
                            area=output[:4]
                            bboxes = xyxy_wide2xyxy_narrow(output[:4])
                            id= int(output[4])
                            cls = int(output[5])
                            label="id:%d conf:%.2f" % (id,conf)
                            annotator.box_label(bboxes, label, color=colors(cls, True))
                            
                            # hist compare
                            target_img=im0s[int(area[1]):int(area[3]),int(area[0]):int(area[2]),:]
                            isValid,hist=self.valSim(fn,id,target_img)
                            if isValid:
                                # crop refresh
                                crop_img_refresh=False
                                if max_conf.get(id):
                                    if conf>max_conf[id]:
                                        max_conf[id]=conf
                                        crop_img_refresh=True
                                else:
                                    max_conf[id]=conf
                                    crop_img_refresh=True
                                
                                if crop_img_refresh:
                                    img_crop=im0s[int(bboxes[1]):int(bboxes[3]),int(bboxes[0]):int(bboxes[2]),:]
                                    img_crop=cv2.cvtColor(img_crop,cv2.COLOR_BGR2RGB)
                                    thread.send_crop_data.emit([id,img_crop,fn])

                            row[id]=[bboxes,hist]
                                         
            self.dataTable.append(row)
            
            # Stream results
            imBox=cv2.cvtColor(imBox,cv2.COLOR_BGR2RGB)
            thread.send_img.emit(imBox)
            previous_frame[i]=current_frame[i]
        
        thread.send_msg.emit(True)
    
    def valSim(self,fn,id,img_crop):
        img_crop_hsv=cv2.cvtColor(img_crop,cv2.COLOR_BGR2HSV)
        hist=cv2.calcHist([img_crop_hsv],[0,1],None,[180,256],[0,180,0,256])
        cv2.normalize(hist,hist,0,1,cv2.NORM_MINMAX)

        previous_fn=fn-100
        if previous_fn<0:
            previous_fn=0
        
        simScore=[]
        for pfn in range(previous_fn,fn):
            data=self.dataTable[pfn].get(id)
            if data is not None:
                pre_hist=data[1]
                validation=[]
                for method in VALIDMETHOD:
                    validation.append(self.calSimScore(hist,pre_hist,method))
                simScore.append(np.sum(validation))
        if len(simScore)>0:
            score=np.mean(simScore)
        else:
            return True,hist
        
        if score>0.8:
            return True,hist
        else:
            return False,hist
    
    def calSimScore(self,hist,pre_hist,method):
        x=cv2.compareHist(hist,pre_hist,method)
        if method==cv2.HISTCMP_CORREL:
            return 0.2*x if x>0 else 0
        elif method==cv2.HISTCMP_CHISQR:
            return math.pow(1.05,(-x))*0.25     #(1.05^(-x))*0.25
        elif method==cv2.HISTCMP_INTERSECT:
            x=x/np.sum(hist)
            return 0.25*x
        else: # cv2.HISTCMP_BHATTACHARYYA
            return 0.3*(-x+1)
        
    def bluring(self,thread,target_ids=[],blur_option={'filter':(0,0),'sigma':7}):
        dataset = LoadImages(self.video_path, self.image_size) 
        self.video_frames=None
        
        for fn,(path, im, im0s, vid_cap, s) in enumerate(dataset):
            if not thread.power:
                break
            if fn==0:
                fps=vid_cap.get(cv2.CAP_PROP_FPS)
                video_len=int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                video_frames=np.zeros((video_len, h, w, 3), dtype=np.uint8)
            
            frame_bboxes=self.dataTable[fn]
            for id in target_ids:
                data=frame_bboxes.get(id)
                if data is not None:
                    bboxes=data[0]
                    im0s[int(bboxes[1]):int(bboxes[3]),int(bboxes[0]):int(bboxes[2]),:]=cv2.GaussianBlur(im0s[int(bboxes[1]):int(bboxes[3]),int(bboxes[0]):int(bboxes[2]),:],blur_option['filter'],blur_option['sigma'])
            
            # showing    
            im0=cv2.cvtColor(im0s,cv2.COLOR_BGR2RGB)
            thread.send_img.emit(im0)
            
            #save
            video_frames[fn]=im0.astype(np.uint8)
        
        self.video_frames=video_frames
        self.fps=fps
        self.video_len=video_len

        thread.send_msg.emit(True)

    def save_video(self,save_dir,file_name):
        save_path=os.path.join(save_dir,file_name)
        if os.path.isfile(save_path):
            pass
        else:
            audio=AudioFileClip(self.video_path)
            duration=self.video_len/self.fps
            bitrate=os.path.getsize(self.video_path)/audio.duration*8 #용량별 적정 bitrate
            #bitrate=w*h*fps  #적정 bitrate (kbps)
            output_video=VideoClip(lambda t: self.video_frames[int(round(t*self.fps))],duration=duration)
            output_video.audio=audio
            output_video.write_videofile(save_path,fps=self.fps,bitrate=str(bitrate))
        
    