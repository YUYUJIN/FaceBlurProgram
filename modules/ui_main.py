# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingnxZcz.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logo_wh.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; font-size: 15px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-movie.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        
        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_14 = QVBoxLayout(self.home)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.home_layout = QFrame(self.home)
        self.home_layout.setObjectName(u"home_layout")
        self.home_layout.setFrameShape(QFrame.StyledPanel)
        self.home_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.home_layout)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.home_left_right_layout = QHBoxLayout()
        self.home_left_right_layout.setObjectName(u"home_left_right_layout")
        self.left_layout = QGridLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.file_tree_layout = QFrame(self.home_layout)
        self.file_tree_layout.setObjectName(u"file_tree_layout")
        self.file_tree_layout.setFrameShape(QFrame.StyledPanel)
        self.file_tree_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.file_tree_layout)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 25)
        self.file_tree = QTreeView(self.file_tree_layout)
        self.file_tree.setObjectName(u"file_tree")

        self.gridLayout_7.addWidget(self.file_tree, 2, 0, 1, 1)

        self.open_folder_btn = QPushButton(self.file_tree_layout)
        self.open_folder_btn.setObjectName(u"open_folder_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.open_folder_btn.sizePolicy().hasHeightForWidth())
        self.open_folder_btn.setSizePolicy(sizePolicy3)
        self.open_folder_btn.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u"./images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_folder_btn.setIcon(icon3)

        self.gridLayout_7.addWidget(self.open_folder_btn, 0, 0, 1, 1)
        self.back_btn = QPushButton(self.file_tree_layout)
        self.back_btn.setObjectName(u"back_btn")
        
        icon4 = QIcon()
        icon4.addFile(u"images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon4)
        self.gridLayout_7.addWidget(self.back_btn, 1, 0, 1, 1)
        self.left_layout.addWidget(self.file_tree_layout, 0, 0, 1, 1)


        self.home_left_right_layout.addLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.file_list_layout = QFrame(self.home_layout)
        self.file_list_layout.setObjectName(u"file_list_layout")
        self.file_list_layout.setFrameShape(QFrame.StyledPanel)
        self.file_list_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.file_list_layout)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 12, -1, -1)
        self.file_list = QListView(self.file_list_layout)
        self.file_list.setObjectName(u"file_list")
        self.file_list.setMovement(QListView.Static)
        self.file_list.setFlow(QListView.TopToBottom)
        self.file_list.setResizeMode(QListView.Fixed)

        self.gridLayout_5.addWidget(self.file_list, 0, 0, 1, 1)


        self.right_layout.addWidget(self.file_list_layout)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.blank_layout = QFrame(self.home_layout)
        self.blank_layout.setObjectName(u"blank_layout")
        self.blank_layout.setFrameShape(QFrame.StyledPanel)
        self.blank_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.blank_layout)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.bottom_layout.addWidget(self.blank_layout)

        self.function_combobox_layout = QFrame(self.home_layout)
        self.function_combobox_layout.setObjectName(u"function_combobox_layout")
        self.function_combobox_layout.setFrameShape(QFrame.StyledPanel)
        self.function_combobox_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.function_combobox_layout)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.function_combobox = QComboBox(self.function_combobox_layout)
        self.function_combobox.addItem("")
        self.function_combobox.addItem("")
        self.function_combobox.setObjectName(u"function_combobox")

        self.gridLayout_3.addWidget(self.function_combobox, 0, 0, 1, 1)


        self.bottom_layout.addWidget(self.function_combobox_layout)

        self.next_btn_layout = QFrame(self.home_layout)
        self.next_btn_layout.setObjectName(u"next_btn_layout")
        self.next_btn_layout.setFrameShape(QFrame.StyledPanel)
        self.next_btn_layout.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.next_btn_layout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.next_btn = QPushButton(self.next_btn_layout)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setFont(font)
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_4.addWidget(self.next_btn, 0, 0, 1, 1)


        self.bottom_layout.addWidget(self.next_btn_layout)

        self.bottom_layout.setStretch(0, 6)
        self.bottom_layout.setStretch(1, 2)
        self.bottom_layout.setStretch(2, 2)

        self.right_layout.addLayout(self.bottom_layout)

        self.right_layout.setStretch(0, 9)
        self.right_layout.setStretch(1, 1)

        self.home_left_right_layout.addLayout(self.right_layout)

        self.home_left_right_layout.setStretch(0, 2)
        self.home_left_right_layout.setStretch(1, 8)

        self.gridLayout_8.addLayout(self.home_left_right_layout, 0, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.home_layout)


        self.stackedWidget.addWidget(self.home)
        self.render = QWidget()
        self.render.setObjectName(u"render")
        self.render.setStyleSheet(u"b")
        self.horizontalLayout_7 = QHBoxLayout(self.render)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.videoplayerArea = QGridLayout()
        self.videoplayerArea.setObjectName(u"videoplayerArea")
        self.controlBox = QVBoxLayout()
        self.controlBox.setObjectName(u"controlBox")
        self.controlBox1 = QHBoxLayout()
        self.controlBox1.setObjectName(u"controlBox1")
        self.playButton = QPushButton(self.render)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setFont(font)
        self.playButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.playButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.controlBox1.addWidget(self.playButton)

        self.pauseButton = QPushButton(self.render)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setFont(font)
        self.pauseButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pauseButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        playIcon = QIcon()
        playIcon.addFile(u"images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseButton.setIcon(playIcon)

        self.controlBox1.addWidget(self.pauseButton)

        self.stopButton = QPushButton(self.render)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setFont(font)
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        stopIcon = QIcon()
        stopIcon.addFile(u"images/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(stopIcon)

        self.controlBox1.addWidget(self.stopButton)

        self.videoSlider = QSlider(self.render)
        self.videoSlider.setObjectName(u"videoSlider")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.controlBox1.addWidget(self.videoSlider)
        self.controlBox1.setStretch(0,1)
        self.controlBox1.setStretch(1,1)
        self.controlBox1.setStretch(2,1)
        self.controlBox1.setStretch(3,7)

        self.controlBox.addLayout(self.controlBox1)

        self.controlBox.setStretch(0,9)
        self.controlBox.setStretch(1,1)

        self.videoplayerArea.addLayout(self.controlBox, 1, 0, 1, 1)

        self.videoScreen = QLabel(self.render)
        self.videoScreen.setObjectName(u"videoScreen")
        self.videoScreen.setAlignment(Qt.AlignCenter)

        self.videoplayerArea.addWidget(self.videoScreen, 0, 0, 1, 1)

        self.videoplayerArea.setRowStretch(0, 7)
        self.videoplayerArea.setRowStretch(1, 3)

        self.horizontalLayout_8.addLayout(self.videoplayerArea)

        self.infoNrenderArea = QVBoxLayout()
        self.infoNrenderArea.setObjectName(u"infoNrenderArea")
        self.pathBox = QGridLayout()
        self.pathBox.setObjectName(u"pathBox")
        self.pathLineEdit = QLineEdit(self.render)
        self.pathLineEdit.setObjectName(u"pathLineEdit")

        self.pathBox.addWidget(self.pathLineEdit, 0, 1, 1, 1)

        self.pathLabel = QLabel(self.render)
        self.pathLabel.setObjectName(u"pathLabel")

        self.pathBox.addWidget(self.pathLabel, 0, 0, 1, 1)

        self.pathButton = QToolButton(self.render)
        self.pathButton.setObjectName(u"pathButton")

        self.pathBox.addWidget(self.pathButton, 0, 2, 1, 1)


        self.infoNrenderArea.addLayout(self.pathBox)

        self.fnameBox = QGridLayout()
        self.fnameBox.setObjectName(u"fnameBox")
        self.fnameLabel = QLabel(self.render)
        self.fnameLabel.setObjectName(u"fnameLabel")

        self.fnameBox.addWidget(self.fnameLabel, 0, 0, 1, 1)

        self.fnameLineEdit = QLineEdit(self.render)
        self.fnameLineEdit.setObjectName(u"fnameLineEdit")

        self.fnameBox.addWidget(self.fnameLineEdit, 0, 1, 1, 1)


        self.infoNrenderArea.addLayout(self.fnameBox)

        
        self.infoBrowser = QLabel(self.render)
        self.infoBrowser.setObjectName(u"infoBrowser")
        self.infoBrowser.setAlignment(Qt.AlignTop)

        self.infoNrenderArea.addWidget(self.infoBrowser)


        # self.infoNrenderArea.addLayout(self.infoBox)

        self.renderBox = QHBoxLayout()
        self.renderBox.setObjectName(u"renderBox")
        self.blank_layout2 = QFrame(self.render)
        self.renderBox.addWidget(self.blank_layout2)
        self.renderButton = QPushButton(self.render)
        self.renderButton.setObjectName(u"renderButton")
        self.renderButton.setFont(font)
        self.renderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.renderButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.renderBox.addWidget(self.renderButton)
        self.renderBox.setStretch(0,6)
        self.renderBox.setStretch(1,4)


        self.infoNrenderArea.addLayout(self.renderBox)

        self.infoNrenderArea.setStretch(0, 1)
        self.infoNrenderArea.setStretch(1, 1)
        self.infoNrenderArea.setStretch(2, 4)
        self.infoNrenderArea.setStretch(3, 1)

        self.horizontalLayout_8.addLayout(self.infoNrenderArea)

        self.horizontalLayout_8.setStretch(0, 7)
        self.horizontalLayout_8.setStretch(1, 3)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.render)

        self.faceTrackPage = QWidget()
        self.faceTrackPage.setObjectName(u"faceTrackPage")
        self.verticalLayout_20 = QVBoxLayout(self.faceTrackPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.visualizeArea = QHBoxLayout()
        self.visualizeArea.setObjectName(u"visualizeArea")
        self.videoPanel = QLabel(self.faceTrackPage)
        self.videoPanel.setObjectName(u"videoPanel")
        self.videoPanel.setAlignment(Qt.AlignCenter)

        self.visualizeArea.addWidget(self.videoPanel)

        self.facePanel = QScrollArea(self.faceTrackPage)
        self.facePanel.setObjectName(u"facePanel")
        self.facePanel.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 18, 18))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.faceLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.faceLayout.setObjectName(u"faceLayout")
        self.facePanel.setWidget(self.scrollAreaWidgetContents)

        self.visualizeArea.addWidget(self.facePanel)

        self.visualizeArea.setStretch(0, 7)
        self.visualizeArea.setStretch(1, 3)

        self.verticalLayout_20.addLayout(self.visualizeArea)

        self.propertyArea = QHBoxLayout()
        self.propertyArea.setObjectName(u"propertyArea")
        self.detectPropBox = QGroupBox(self.faceTrackPage)
        self.detectPropBox.setObjectName(u"detectPropBox")
        self.gridLayout = QGridLayout(self.detectPropBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configLayout = QVBoxLayout()
        self.configLayout.setObjectName(u"configLayout")
        self.config1Label = QLabel(self.detectPropBox)
        self.config1Label.setObjectName(u"config1Label")

        self.configLayout.addWidget(self.config1Label)

        self.config1Layout = QHBoxLayout()
        self.config1Layout.setObjectName(u"config1Layout")
        self.config1Box = QDoubleSpinBox(self.detectPropBox)
        self.config1Box.setObjectName(u"config1Box")
        self.config1Box.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.config1Box.setDecimals(2)
        self.config1Box.setMinimum(0.500000000000000)
        self.config1Box.setMaximum(0.900000000000000)
        self.config1Box.setSingleStep(0.050000000000000)
        self.config1Box.setValue(0.600000000000000)

        self.config1Layout.addWidget(self.config1Box)

        self.config1Bar = QSlider(self.detectPropBox)
        self.config1Bar.setObjectName(u"config1Bar")
        self.config1Bar.setMinimum(50)
        self.config1Bar.setMaximum(90)
        self.config1Bar.setSingleStep(5)
        self.config1Bar.setPageStep(5)
        self.config1Bar.setValue(60)
        self.config1Bar.setOrientation(Qt.Horizontal)
        self.config1Bar.setTickPosition(QSlider.NoTicks)

        self.config1Layout.addWidget(self.config1Bar)


        self.configLayout.addLayout(self.config1Layout)

        self.config2Label = QLabel(self.detectPropBox)
        self.config2Label.setObjectName(u"config2Label")

        self.configLayout.addWidget(self.config2Label)

        self.config2Layout = QHBoxLayout()
        self.config2Layout.setObjectName(u"config2Layout")
        self.config2Box = QDoubleSpinBox(self.detectPropBox)
        self.config2Box.setObjectName(u"config2Box")
        self.config2Box.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.config2Box.setWrapping(False)
        self.config2Box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.config2Box.setDecimals(3)
        self.config2Box.setMinimum(0.500000000000000)
        self.config2Box.setMaximum(1.000000000000000)
        self.config2Box.setSingleStep(0.005000000000000)
        self.config2Box.setValue(0.995000000000000)

        self.config2Layout.addWidget(self.config2Box)

        self.config2Bar = QSlider(self.detectPropBox)
        self.config2Bar.setObjectName(u"config2Bar")
        self.config2Bar.setMinimum(500)
        self.config2Bar.setMaximum(1000)
        self.config2Bar.setSingleStep(5)
        self.config2Bar.setPageStep(5)
        self.config2Bar.setValue(995)
        self.config2Bar.setSliderPosition(995)
        self.config2Bar.setOrientation(Qt.Horizontal)

        self.config2Layout.addWidget(self.config2Bar)


        self.configLayout.addLayout(self.config2Layout)

        self.config3Label = QLabel(self.detectPropBox)
        self.config3Label.setObjectName(u"config3Label")

        self.configLayout.addWidget(self.config3Label)

        self.config3Layout = QHBoxLayout()
        self.config3Layout.setObjectName(u"config3Layout")
        self.config3Box = QDoubleSpinBox(self.detectPropBox)
        self.config3Box.setObjectName(u"config3Box")
        self.config3Box.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.config3Box.setDecimals(1)
        self.config3Box.setMinimum(0.500000000000000)
        self.config3Box.setMaximum(0.900000000000000)
        self.config3Box.setSingleStep(0.100000000000000)
        self.config3Box.setValue(0.700000000000000)

        self.config3Layout.addWidget(self.config3Box)

        self.config3Bar = QSlider(self.detectPropBox)
        self.config3Bar.setObjectName(u"config3Bar")
        self.config3Bar.setMinimum(50)
        self.config3Bar.setMaximum(90)
        self.config3Bar.setPageStep(1)
        self.config3Bar.setValue(70)
        self.config3Bar.setOrientation(Qt.Horizontal)

        self.config3Layout.addWidget(self.config3Bar)


        self.configLayout.addLayout(self.config3Layout)

        self.config45Layout = QHBoxLayout()
        self.config45Layout.setObjectName(u"config45Layout")
        self.config4Label = QLabel(self.detectPropBox)
        self.config4Label.setObjectName(u"config4Label")

        self.config45Layout.addWidget(self.config4Label)

        self.config4Box = QSpinBox(self.detectPropBox)
        self.config4Box.setObjectName(u"config4Box")
        self.config4Box.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.config4Box.setMinimum(24)
        self.config4Box.setMaximum(150)
        self.config4Box.setValue(30)

        self.config45Layout.addWidget(self.config4Box)

        self.config5Label = QLabel(self.detectPropBox)
        self.config5Label.setObjectName(u"config5Label")

        self.config45Layout.addWidget(self.config5Label)

        self.config5Box = QSpinBox(self.detectPropBox)
        self.config5Box.setObjectName(u"config5Box")
        self.config5Box.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.config5Box.setMinimum(100)
        self.config5Box.setMaximum(500)
        self.config5Box.setValue(100)

        self.config45Layout.addWidget(self.config5Box)


        self.configLayout.addLayout(self.config45Layout)


        self.gridLayout.addLayout(self.configLayout, 0, 0, 1, 1)

        self.detectButton = QPushButton(self.detectPropBox)
        self.detectButton.setObjectName(u"detectButton")
        self.detectButton.setMinimumSize(QSize(0, 0))
        self.detectButton.setFont(font)
        self.detectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.detectButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout.addWidget(self.detectButton, 2, 1, 1, 1)

        self.detectDefaultButton = QPushButton(self.detectPropBox)
        self.detectDefaultButton.setObjectName(u"detectDefaultButton")
        self.detectDefaultButton.setMinimumSize(QSize(0, 0))
        self.detectDefaultButton.setFont(font)
        self.detectDefaultButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.detectDefaultButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout.addWidget(self.detectDefaultButton, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 8)
        self.gridLayout.setColumnStretch(1, 2)

        self.propertyArea.addWidget(self.detectPropBox)

        self.blurPropBox = QGroupBox(self.faceTrackPage)
        self.blurPropBox.setObjectName(u"blurPropBox")
        self.gridLayout_2 = QGridLayout(self.blurPropBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.detectButton_2 = QPushButton(self.blurPropBox)
        self.detectButton_2.setObjectName(u"detectButton_2")
        self.detectButton_2.setMinimumSize(QSize(0, 0))
        self.detectButton_2.setFont(font)
        self.detectButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.detectButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.detectButton_2, 3, 1, 1, 1)

        self.blut1Layout = QVBoxLayout()
        self.blut1Layout.setObjectName(u"blut1Layout")
        self.blur1Label = QLabel(self.blurPropBox)
        self.blur1Label.setObjectName(u"blur1Label")

        self.blut1Layout.addWidget(self.blur1Label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.blur1Box = QSpinBox(self.blurPropBox)
        self.blur1Box.setObjectName(u"blur1Box")
        self.blur1Box.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.blur1Box.setMinimum(5)
        self.blur1Box.setMaximum(11)
        self.blur1Box.setValue(7)

        self.horizontalLayout_6.addWidget(self.blur1Box)

        self.blur1Bar = QSlider(self.blurPropBox)
        self.blur1Bar.setObjectName(u"blur1Bar")
        self.blur1Bar.setMinimum(5)
        self.blur1Bar.setMaximum(11)
        self.blur1Bar.setValue(7)
        self.blur1Bar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.blur1Bar)


        self.blut1Layout.addLayout(self.horizontalLayout_6)


        self.gridLayout_2.addLayout(self.blut1Layout, 0, 0, 1, 1)

        self.detectDefaultButton_2 = QPushButton(self.blurPropBox)
        self.detectDefaultButton_2.setObjectName(u"detectDefaultButton_2")
        self.detectDefaultButton_2.setMinimumSize(QSize(0, 0))
        self.detectDefaultButton_2.setFont(font)
        self.detectDefaultButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.detectDefaultButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.detectDefaultButton_2, 2, 1, 1, 1)

        self.frame = QFrame(self.blurPropBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 3)
        self.gridLayout_2.setColumnStretch(0, 8)
        self.gridLayout_2.setColumnStretch(1, 2)

        self.propertyArea.addWidget(self.blurPropBox)

        self.propertyArea.setStretch(0, 5)
        self.propertyArea.setStretch(1, 5)

        self.verticalLayout_20.addLayout(self.propertyArea)

        self.saveButtonArea = QHBoxLayout()
        self.saveButtonArea.setObjectName(u"saveButtonArea")
        self.frame_2 = QFrame(self.faceTrackPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.saveButtonArea.addWidget(self.frame_2)

        self.saveButton = QPushButton(self.faceTrackPage)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 0))
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.saveButtonArea.addWidget(self.saveButton)

        self.saveButtonArea.setStretch(0, 9)
        self.saveButtonArea.setStretch(1, 1)

        self.verticalLayout_20.addLayout(self.saveButtonArea)

        self.verticalLayout_20.setStretch(0, 6)
        self.verticalLayout_20.setStretch(1, 4)
        self.stackedWidget.addWidget(self.faceTrackPage)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Blah Blur", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"blur anonymous", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Blah Blur", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")

        self.open_folder_btn.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.back_btn.setText('')
        self.function_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Blur Face", None))
        self.function_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Extra Function", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.videoScreen.setText(QCoreApplication.translate("MainWindow", u"Video Player", None))
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"path", None))
        self.pathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.fnameLabel.setText(QCoreApplication.translate("MainWindow", u"file name", None))
        self.renderButton.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.videoPanel.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.detectPropBox.setTitle(QCoreApplication.translate("MainWindow", u"Detection Properties", None))
        self.config1Label.setText(QCoreApplication.translate("MainWindow", u"Detection Confidence", None))
        self.config1Label.setToolTip(QCoreApplication.translate("MainWindow", u"Set face detection sensitivity", None))
        self.config2Label.setText(QCoreApplication.translate("MainWindow", u"MC Lambda", None))
        self.config2Label.setToolTip(QCoreApplication.translate("MainWindow", u"Matching with both appearance (1 - MC_LAMBDA) and motion cost", None))
        self.config3Label.setText(QCoreApplication.translate("MainWindow", u"EMA Alpha", None))
        self.config3Label.setToolTip(QCoreApplication.translate("MainWindow", u"Updates  appearance  state in  an exponential moving average manner", None))
        self.config4Label.setText(QCoreApplication.translate("MainWindow", u"Max Age", None))
        self.config4Label.setToolTip(QCoreApplication.translate("MainWindow", u"Maximum number of missed misses before a track is deleted", None))
        self.config5Label.setText(QCoreApplication.translate("MainWindow", u"NN Budget", None))
        self.config5Label.setToolTip(QCoreApplication.translate("MainWindow", u"Maximum size of the appearance descriptors gallery", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.detectDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.blurPropBox.setTitle(QCoreApplication.translate("MainWindow", u"Blur Properties", None))
        self.detectButton_2.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.blur1Label.setText(QCoreApplication.translate("MainWindow", u"Blur intensity", None))
        self.detectDefaultButton_2.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Team3", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

