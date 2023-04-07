import sys
import os
from PySide6 import QtWidgets
from PySide6.QtCore import QThread,Signal,QSize,Qt
from PySide6 import QtGui

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

import cv2
import copy
import torch
import numpy as np
from face_module.yolo_sort import FaceTracker
from ui_loading import LoadingScreen

class TrackingThread(QThread):
    send_img=Signal(np.ndarray)
    send_crop_data=Signal(list)
    send_msg=Signal(bool)
    
    def __init__(self,trackingModule):
        super(TrackingThread,self).__init__()
        self.module=trackingModule
        self.conf=0.5
        self.sort_option={}
        self.power=True

    @torch.no_grad()
    def run(self):
        self.module.tracking(self.conf,self.sort_option,self)

    def stop(self):
        self.power = False
        self.quit()
        self.wait(3000)

class BlurThread(QThread):
    send_img=Signal(np.ndarray)
    send_msg=Signal(bool)
    
    def __init__(self,trackingModule):
        super(BlurThread,self).__init__()
        self.module=trackingModule
        self.target_id=[]
        self.blur_option={}
        self.power=True

    def run(self):
        self.module.bluring(self,self.target_id,self.blur_option)

    def stop(self):
        self.power = False
        self.quit()
        self.wait(3000)

class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)
    position_changed = Signal(int)

    def __init__(self, video_frames):
        super().__init__()
        self.video_frames=video_frames
        self.is_playing = True
        self.is_paused = False
        self.current_frame = None
        self.position=0

    def run(self):
        fn=0
        while fn<len(self.video_frames):
            if self.is_playing:
                if not self.is_paused:
                    if self.current_frame is not None:
                        fn=self.current_frame
                        self.current_frame = None
                    self.position=fn
                    frame=self.video_frames[fn]
                    h, w, ch = frame.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    self.change_pixmap_signal.emit(qt_image)

                    self.position_changed.emit(self.position)
                    fn+=1

            self.msleep(30)
        widgets.playButton.setEnabled(True)
        widgets.pauseButton.setEnabled(False)
        self.quit()

    def stop(self):
        self.is_playing = False
        self.cap.release()
        self.quit()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

# SET AS GLOBAL WIDGETS
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.loading=LoadingScreen()

        # thread
        self.demo=FaceTracker(device='')
        self.trackT=None
        self.blurT=None

        self.loading.stopAnimation()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "Blah Blur"
        description = "Blah Blur"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        
        widgets.open_folder_btn.clicked.connect(self.open_folder_btn_event)
        widgets.file_list.clicked.connect(self.list_view_clicked)
        widgets.file_list.doubleClicked.connect(self.list_view_double_clicked)
        widgets.file_tree.clicked.connect(self.CopyFilePath)
        widgets.next_btn.clicked.connect(self.next_btn_event)
        widgets.back_btn.clicked.connect(self.back_btn_event)

        widgets.saveButton.setDisabled(True)
        widgets.detectButton_2.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        widgets.detectButton_2.setDisabled(True)
        widgets.config3Box.setDecimals(2)
        widgets.blur1Bar.setPageStep(1)

        em_frame_1 = QtWidgets.QFrame()
        em_frame_2 = QtWidgets.QFrame()
        widgets.faceLayout.addWidget(em_frame_1, 0, 0)
        widgets.faceLayout.addWidget(em_frame_2, 0, 1)
        widgets.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        widgets.config1Box.valueChanged.connect(self.box2bar)
        widgets.config2Box.valueChanged.connect(self.box2bar)
        widgets.config3Box.valueChanged.connect(self.box2bar)
        widgets.blur1Box.valueChanged.connect(self.box2bar)

        widgets.config1Bar.valueChanged.connect(self.bar2box)
        widgets.config2Bar.valueChanged.connect(self.bar2box)
        widgets.config3Bar.valueChanged.connect(self.bar2box)
        widgets.blur1Bar.valueChanged.connect(self.bar2box)

        widgets.detectDefaultButton.clicked.connect(self.set_default)
        widgets.detectDefaultButton_2.clicked.connect(self.set_default)

        widgets.detectButton.clicked.connect(self.detect_face)
        widgets.detectButton_2.clicked.connect(self.blur_face)
        widgets.saveButton.clicked.connect(self.save_btn_event)

        widgets.pathButton.clicked.connect(self.setPathButton)
        widgets.pathLineEdit.returnPressed.connect(self.setPathLineEdit)
        widgets.renderButton.clicked.connect(self.setRenderButton)
        widgets.renderButton.setEnabled(False)

        widgets.playButton.clicked.connect(self.play_video)
        widgets.stopButton.clicked.connect(self.stop_video)
        widgets.pauseButton.clicked.connect(self.resume_video)

        widgets.videoSlider.sliderPressed.connect(self.stop_bar)
        widgets.videoSlider.sliderReleased.connect(self.resume_bar)
        widgets.videoSlider.sliderReleased.connect(lambda : self.on_slider_moved(widgets.videoSlider.value()))

        self.current_frame = 0

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"
        self.testNum=0
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.render)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.faceTrackPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
    
    def open_folder_btn_event(self):
        self.fname = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')

        # 해당 폴더의 root
        self.root_path = self.fname
        self.Model_file_system = QtWidgets.QFileSystemModel()
        self.Model_file_system.setRootPath(self.root_path)
        self.Model_file_system.setReadOnly(True)
        self.Model_file_system.setNameFilters([''])    # mp4 파일만 받게 함
        self.Model_file_system.setNameFilterDisables(False) # 파일 이름 바꾸기 X
        self.Model_file_list = QtWidgets.QFileSystemModel()
        self.Model_file_list.setRootPath(self.root_path)
        self.Model_file_list.setReadOnly(True)
        self.Model_file_list.setNameFilters(['*.mp4'])
        self.Model_file_list.setNameFilterDisables(False)
        widgets.file_tree.setModel(self.Model_file_system)
        widgets.file_tree.setRootIndex(self.Model_file_system.index(self.root_path))
        widgets.file_tree.setHeaderHidden(True)
        widgets.file_tree.setRootIsDecorated(True)  
        widgets.file_tree.setAllColumnsShowFocus(False)
        widgets.file_tree.hideColumn(1)
        widgets.file_tree.hideColumn(2)
        widgets.file_tree.hideColumn(3)
        widgets.file_list.setModel(self.Model_file_list)
        widgets.file_list.setRootIndex(self.Model_file_list.index(self.root_path))
        widgets.file_list.setFlow(QtWidgets.QListView.LeftToRight)
        widgets.file_list.setResizeMode(QtWidgets.QListView.Adjust)
        widgets.file_list.setViewMode(QtWidgets.QListView.IconMode)
        widgets.file_list.setGridSize(QSize(120, 120))
        widgets.file_list.setIconSize(QSize(80, 80))
    def back_btn_event(self, index):
        widgets.file_list.setRootIndex(self.Model_file_list.index(self.root_path))
        widgets.file_tree.collapseAll()
    def list_view_clicked(self, index):
        self.list_path = self.Model_file_list.filePath(index)
        self.only_mp4 = os.path.splitext(self.list_path)[-1]

    def list_view_double_clicked(self, index):
        self.list_path_double = self.Model_file_list.filePath(index)
        if self.only_mp4 != '.mp4':
            widgets.file_list.setRootIndex(index)
        widgets.file_tree.setCurrentIndex(self.Model_file_system.index(self.list_path_double))
    
    
 
    def CopyFilePath(self, index):
        self.tree_path = self.Model_file_system.filePath(index)
        widgets.file_list.setRootIndex(self.Model_file_list.index(self.tree_path))
        widgets.file_tree.setCurrentIndex(index)
        widgets.file_tree.collapseAll()
        widgets.file_tree.expand(index)

    def next_btn_event(self):
        try:
            if os.path.splitext(self.list_path)[-1] == '.mp4':
                widgets.stackedWidget.setCurrentWidget(widgets.faceTrackPage)
                UIFunctions.resetStyle(self, widgets.btn_new.objectName)
                widgets.btn_new.setStyleSheet(UIFunctions.selectMenu(widgets.btn_new.styleSheet()))
                self.demo.video_path = copy.deepcopy(self.list_path)
            else :
                QtWidgets.QMessageBox.information(self,'video not found','video not found')
        except:
            QtWidgets.QMessageBox.information(self,'video not found','video not found')

    def box2bar(self, i):
        box = self.sender()
        boxName = box.objectName()

        if boxName == 'config1Box':
            widgets.config1Bar.setValue(i*100)
        if boxName == 'config2Box':
            widgets.config2Bar.setValue(i*1000)
        if boxName == 'config3Box':
            widgets.config3Bar.setValue(i*100)
        if boxName == 'blur1Box':
            widgets.blur1Bar.setValue(i)
   
    def bar2box(self, i):
        bar = self.sender()
        barName = bar.objectName()

        if barName == 'config1Bar':
            widgets.config1Box.setValue(i/100)
        if barName == 'config2Bar':
            widgets.config2Box.setValue(i/1000)
        if barName == 'config3Bar':
            widgets.config3Box.setValue(i/100)
        if barName == 'blur1Bar':
            widgets.blur1Box.setValue(i)

    def set_default(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'detectDefaultButton':
            widgets.config1Box.setValue(0.6)
            widgets.config2Box.setValue(0.995)
            widgets.config3Box.setValue(0.7)
            widgets.config4Box.setValue(30)
            widgets.config5Box.setValue(100)
        if btnName == 'detectDefaultButton_2':
            widgets.blur1Box.setValue(7)

    def save_btn_event(self):
        widgets.stackedWidget.setCurrentWidget(widgets.render)
        UIFunctions.resetStyle(self, "btn_widgets")
        widgets.btn_widgets.setStyleSheet(UIFunctions.selectMenu(widgets.btn_widgets.styleSheet()))
        widgets.infoBrowser.setText(f'''
        Detection confidence : {self.trackT.conf}
        MC lambda : {self.trackT.sort_option['MC_LAMBDA']}
        EMA alpha : {self.trackT.sort_option['EMA_ALPHA']}
        Max age : {self.trackT.sort_option['MAX_AGE']}
        NN budget : {self.trackT.sort_option['NN_BUDGET']}
        Blur intensity : {self.blurT.blur_option['sigma']}
        ''')
        widgets.renderButton.setEnabled(True)

    def setPathButton(self):
        fpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open Folder')
        widgets.pathLineEdit.setText(fpath)
        
    def setPathLineEdit(self):
        self.setText(self.path[0])

    def setRenderButton(self):
        widgets.renderButton.setText('Saving...')
        widgets.renderButton.setEnabled(False)
        QCoreApplication.processEvents()
        filename = widgets.fnameLineEdit.text()
        filepath=widgets.pathLineEdit.text()
        self.demo.save_video(filepath,filename+'.mp4')
        widgets.renderButton.setText('Render')
        widgets.renderButton.setEnabled(True)

    def detect_face(self):
        #스레드 초기화
        if self.trackT is not None:
            self.trackT.stop()
        self.trackT=TrackingThread(self.demo)
        self.trackT.send_img.connect(lambda x: self.show_img(x,widgets.videoPanel))
        self.trackT.send_msg.connect(lambda x: self.end_detection(x))
        self.trackT.send_crop_data.connect(lambda x: self.crop_refresh(x))

        widgets.detectButton_2.setDisabled(True) # set Blur btn disabled
        self.faceIdList = []
        self._clear_face()
        
        conf=widgets.config1Box.value()
        sort_option=dict()
        sort_option['ECC']= True                                    # activate camera motion compensation
        sort_option['MC_LAMBDA']= widgets.config2Box.value()        # matching with both appearance (1 - MC_LAMBDA) and motion cost
        sort_option['EMA_ALPHA']= widgets.config3Box.value()         # updates  appearance  state in  an exponential moving average manner
        sort_option['MAX_DIST']= 0.2                                # The matching threshold. Samples with larger distance are considered an invalid match
        sort_option['MAX_IOU_DISTANCE']= 0.7                        # Gating threshold. Associations with cost larger than this value are disregarded.
        sort_option['MAX_AGE']= widgets.config4Box.value()           # Maximum number of missed misses before a track is deleted
        sort_option['N_INIT']= 3                                   # Number of frames that a track remains in initialization phase
        sort_option['NN_BUDGET']= widgets.config5Box.value()        # Maximum size of the appearance descriptors gallery
        
        self.trackT.conf=conf
        self.trackT.sort_option=sort_option
        self.trackT.start()

    def blur_face(self):
        #스레드 초기화
        if self.blurT is not None:
            self.blurT.stop()
        self.blurT=BlurThread(self.demo)
        self.blurT.send_img.connect(lambda x: self.show_img(x,widgets.videoPanel))
        self.blurT.send_msg.connect(lambda x: self.end_bluring(x))

        widgets.detectButton.setDisabled(True) 
        blur_option=dict()
        blur_option['filter']=(0,0)
        blur_option['sigma']=widgets.blur1Box.value()
        
        id_list = []
        for id in self.faceIdList:
            if not getattr(widgets, f'faceButton_{id}').isChecked():
                id_list.append(id)

        self.blurT.target_id=id_list
        self.blurT.blur_option=blur_option
        self.blurT.start()
    
    @staticmethod
    def show_img(image,Qlabel):
        im0=cv2.resize(image,(Qlabel.width(),Qlabel.height()))
        h,w,c=im0.shape
        qImg=QtGui.QImage(im0.data,w,h,w*c,QtGui.QImage.Format_RGB888)
        pixmap=QtGui.QPixmap.fromImage(qImg)
        Qlabel.setPixmap(pixmap)

    def end_detection(self,signal):
        if signal:
            QMessageBox.information(self, 'Complete', 'Detection Completed') # Complete Message
            widgets.detectButton_2.setDisabled(False) # set Blur btn able
            signal=False

    def end_bluring(self,signal):
        if signal:
            QMessageBox.information(self, 'Complete', 'Blur Completed')
            widgets.detectButton.setDisabled(False)
            widgets.saveButton.setDisabled(False)
            signal=False
    
    def crop_refresh(self,signal):
        id=signal[0]
        croped_img=signal[1]
        self.testNum+=1
        if hasattr(widgets, f'faceButton_{id}'):
            Qbutton = getattr(widgets, f'faceButton_{id}')
            im0=cv2.resize(croped_img,(150, 150))
            h,w,c=im0.shape
            qImg=QtGui.QImage(im0.data,w,h,w*c,QtGui.QImage.Format_RGB888)
            pixmap=QtGui.QPixmap.fromImage(qImg)
            icon = QtGui.QIcon(pixmap)
            Qbutton.setIcon(icon)
            Qbutton.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
            Qbutton.setIconSize(QSize(150, 150))
        else:
            setattr(widgets, f'faceButton_{id}', QtWidgets.QToolButton(widgets.facePanel))
            Qbutton = getattr(widgets, f'faceButton_{id}')
            Qbutton.setObjectName(u'faceButton_{}'.format(id))
            Qbutton.setCheckable(True)
            Qbutton.setToolButtonStyle(Qt.ToolButtonStyle(3))
            Qbutton.setStyleSheet('background-color: rgb(33,37,43);')
            Qbutton.setText(f'{id}')
            im0=cv2.resize(croped_img,(150, 150))
            h,w,c=im0.shape
            qImg=QtGui.QImage(im0.data,w,h,w*c,QtGui.QImage.Format_RGB888)
            pixmap=QtGui.QPixmap.fromImage(qImg)
            icon = QtGui.QIcon(pixmap)
            Qbutton.setIcon(icon)
            Qbutton.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
            Qbutton.setIconSize(QSize(150, 150))
            widgets.faceLayout.addWidget(Qbutton, (id-1) // 2, (id-1) % 2)
            widgets.faceLayout.setColumnStretch(0,5)
            widgets.faceLayout.setColumnStretch(1,5)
            self.faceIdList.append(id)

    def _clear_face(self):
        for i in range(widgets.faceLayout.count()):
            child = widgets.faceLayout.itemAt(i).widget()
            try:
                delattr(widgets,child.objectName())
            except:
                pass
            child.deleteLater()

        em_frame_1 = QtWidgets.QFrame()
        em_frame_2 = QtWidgets.QFrame()
        widgets.faceLayout.addWidget(em_frame_1, 0, 0)
        widgets.faceLayout.addWidget(em_frame_2, 0, 1)

    def play_video(self):
        self.thread = VideoThread(self.demo.video_frames)
        self.thread.change_pixmap_signal.connect(lambda x:self.show_video(x, widgets.videoScreen))
        self.thread.position_changed.connect(self.update_slider_position)
        self.thread.start()

        self.update_slider_range()
        
        widgets.playButton.setEnabled(False)
        widgets.pauseButton.setEnabled(False)
        widgets.stopButton.setEnabled(True)

    @staticmethod
    def show_video(image,Qlabel):
        qImg = image.scaled(Qlabel.width(),Qlabel.height())
        pixmap=QtGui.QPixmap.fromImage(qImg)
        Qlabel.setPixmap(pixmap)

    def stop_video(self):
        self.thread.pause()
        widgets.playButton.setEnabled(True)
        widgets.pauseButton.setEnabled(True)
        widgets.stopButton.setEnabled(False)

    def resume_video(self):
        self.thread.resume()
        widgets.playButton.setEnabled(False)
        widgets.pauseButton.setEnabled(False)
        widgets.stopButton.setEnabled(True)

################ slider ########################################################
    def update_slider_range(self):
        video_length = len(self.thread.video_frames)-1
        widgets.videoSlider.setRange(0, video_length)

    def on_slider_moved(self, position):
        self.current_frame = position
        self.thread.current_frame = position

    def update_slider_position(self):
        position = self.thread.position
        widgets.videoSlider.setValue(position)

    def stop_bar(self):
        if not widgets.playButton.isEnabled(): self.thread.pause()
    
    def resume_bar(self):
        if not widgets.playButton.isEnabled(): self.thread.resume()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
