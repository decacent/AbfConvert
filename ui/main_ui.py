# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import ui.ui_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(310, 303)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(310, 303))
        MainWindow.setMaximumSize(QSize(310, 303))
        icon = QIcon()
        icon.addFile(u":/logo/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/logo/Open.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        icon2 = QIcon()
        icon2.addFile(u":/logo/folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenFolder.setIcon(icon2)
        self.actionClearAllFiles = QAction(MainWindow)
        self.actionClearAllFiles.setObjectName(u"actionClearAllFiles")
        icon3 = QIcon()
        icon3.addFile(u":/logo/clear.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClearAllFiles.setIcon(icon3)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon4 = QIcon()
        icon4.addFile(u":/logo/close.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionaboutmenu = QAction(MainWindow)
        self.actionaboutmenu.setObjectName(u"actionaboutmenu")
        icon5 = QIcon()
        icon5.addFile(u":/logo/about.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionaboutmenu.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 233, 291, 20))
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.RunButton = QPushButton(self.centralwidget)
        self.RunButton.setObjectName(u"RunButton")
        self.RunButton.setGeometry(QRect(180, 190, 114, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 54, 12))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 0, 116, 181))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox_initFile = QComboBox(self.layoutWidget)
        self.comboBox_initFile.addItem("")
        self.comboBox_initFile.setObjectName(u"comboBox_initFile")

        self.verticalLayout_2.addWidget(self.comboBox_initFile)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_aimfile = QComboBox(self.layoutWidget)
        self.comboBox_aimfile.addItem("")
        self.comboBox_aimfile.addItem("")
        self.comboBox_aimfile.addItem("")
        self.comboBox_aimfile.addItem("")
        self.comboBox_aimfile.setObjectName(u"comboBox_aimfile")

        self.verticalLayout.addWidget(self.comboBox_aimfile)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.isSplitCheck = QRadioButton(self.layoutWidget)
        self.isSplitCheck.setObjectName(u"isSplitCheck")
        self.isSplitCheck.setContextMenuPolicy(Qt.NoContextMenu)
        self.isSplitCheck.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.isSplitCheck, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_4)

        self.spinBox_timestep = QSpinBox(self.layoutWidget)
        self.spinBox_timestep.setObjectName(u"spinBox_timestep")
        sizePolicy.setHeightForWidth(self.spinBox_timestep.sizePolicy().hasHeightForWidth())
        self.spinBox_timestep.setSizePolicy(sizePolicy)
        self.spinBox_timestep.setMinimumSize(QSize(40, 25))
        self.spinBox_timestep.setMaximumSize(QSize(40, 25))
        self.spinBox_timestep.setMinimum(1)
        self.spinBox_timestep.setMaximum(1000000000)
        self.spinBox_timestep.setSingleStep(1)
        self.spinBox_timestep.setValue(5)

        self.horizontalLayout.addWidget(self.spinBox_timestep)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 30, 161, 192))
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 310, 23))
        self.FileMenu = QMenu(self.menubar)
        self.FileMenu.setObjectName(u"FileMenu")
        self.aboutmenu = QMenu(self.menubar)
        self.aboutmenu.setObjectName(u"aboutmenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.FileMenu.menuAction())
        self.menubar.addAction(self.aboutmenu.menuAction())
        self.FileMenu.addAction(self.actionOpen)
        self.FileMenu.addAction(self.actionOpenFolder)
        self.FileMenu.addAction(self.actionClearAllFiles)
        self.FileMenu.addAction(self.actionExit)
        self.aboutmenu.addAction(self.actionaboutmenu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AbfConvert", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
#if QT_CONFIG(shortcut)
        self.actionOpenFolder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClearAllFiles.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6240\u6709\u6587\u4ef6", None))
#if QT_CONFIG(shortcut)
        self.actionClearAllFiles.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionaboutmenu.setText(QCoreApplication.translate("MainWindow", u"aboutmenu", None))
        self.RunButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5217\u8868", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u6587\u4ef6\u683c\u5f0f", None))
        self.comboBox_initFile.setItemText(0, QCoreApplication.translate("MainWindow", u"Axon(.abf\uff09", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6\u683c\u5f0f", None))
        self.comboBox_aimfile.setItemText(0, QCoreApplication.translate("MainWindow", u"Matlab(.mat)", None))
        self.comboBox_aimfile.setItemText(1, QCoreApplication.translate("MainWindow", u"TextFile(.csv)", None))
        self.comboBox_aimfile.setItemText(2, QCoreApplication.translate("MainWindow", u"TextFile(.txt)", None))
        self.comboBox_aimfile.setItemText(3, QCoreApplication.translate("MainWindow", u"Labview(.tdms)", None))

        self.isSplitCheck.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5206\u6bb5\uff1f\n"
"(Text\u6587\u4ef6\u9002\u7528)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TimeStep(s)", None))
        self.spinBox_timestep.setSpecialValueText("")
        self.spinBox_timestep.setSuffix("")
        self.FileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.aboutmenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

