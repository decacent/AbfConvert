# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(364, 332)
        icon = QIcon()
        icon.addFile(u":/logo/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(80, 10, 256, 281))
        self.textBrowser.setStyleSheet(u"background-color: rgba(52, 152, 219, 0);\n"
"\n"
"")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 61, 61))
        self.widget.setStyleSheet(u"image:url(:/logo/logo.ico)")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 300, 75, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8eAbfConvert", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">About AbfConvert</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AbfConver\u7528\u4e8e\u5c06Axon Clampex\u83b7\u53d6\u7684.abf &gt; 2.0\u7248\u672c\u7684\u6587\u4ef6\u8f6c\u6362\u6210\u5e38\u7528\u7684\u517c\u5bb9\u683c\u5f0f\uff0c\u5305\u62ecMatlab .mat \u6587\u4ef6\u3001\u6587\u672c\u6587\u4ef6 .csv\u548c.txt\u3001\u4ee5\u53caLabview\u652f\u6301\u7684.tdms\u6587\u4ef6\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">.mat \u683c\u5f0f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u517c\u5bb9\u6027\u597d\uff0c\u63a8\u8350\u683c\u5f0f\u3002\u4e0d\u652f\u6301\u5206\u6bb5\uff0c\u652f\u6301\u591a\u901a\u9053\u548c\u591asweep\u626b\u63cf\u683c\u5f0f\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u6587\u672c\u6587\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u652f\u6301\u6309\u65f6\u957f\u5206\u5206\u6bb5\u622a\u53d6\u4fdd\u5b58\u3002\u652f\u6301\u591a\u901a\u9053\u548c\u591asweep\u626b\u63cf\u683c\u5f0f\u3002\u517c\u5bb9\u6027\u597d\uff0c\u4f46\u6587\u4ef6\u4f53\u79ef\u8f83\u5927\uff0c\u4e0d\u63a8\u8350\u4f7f\u7528\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">.tdms\u683c\u5f0f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7c7b\u578b\u652f\u6301\u540c.mat\u6587\u4ef6\uff0c\u6570\u636e\u5c06\u88ab\u8f6c\u6362\u6210Labview\u652f\u6301\u7684\u6ce2\u5f62\u6570\u636e\uff0c\u53ef\u4ee5\u7528\u4e8e\u6570\u636e\u7684\u91cd\u65b0"
                        "\u91c7\u96c6\u590d\u73b0\u3002</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

