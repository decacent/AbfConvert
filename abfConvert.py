# -*- coding: utf-8 -*-

import os, sys, glob
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QSplashScreen, QDialog
from PySide2 import QtCore, QtGui, QtWidgets

from ui.main_ui import Ui_MainWindow
from sub.abfconvertIO import Convert
from ui.about import  Ui_Dialog

def error(func,**kwargs):
    def wrapper(self, *args, **kwargs):
        try:
            u = func(self,**kwargs)
            return u
        except Exception as e:
            QMessageBox.information(self, self.tr("Notice"), self.tr(traceback.format_exc()), QMessageBox.Ok)
    return wrapper

class Worker(QtCore.QThread):
    progressBarValue  = QtCore.Signal(list)
    def __init__(self,files,suffix,issplit=True,timesteps=5):
        super(Worker, self).__init__()
        self.tempfile=files
        self.suffix=suffix
        self.issplit=issplit
        self.timesteps=timesteps
    
    def run(self):
        for index,j in enumerate(self.tempfile):
            temp=Convert(j)
            temp.toCsvTxt(suffix=self.suffix,
            issplit=self.issplit,
            timesteps=self.timesteps)
            self.progressBarValue.emit([(index+1)/len(self.tempfile)*100,0])
        self.progressBarValue.emit([(index+1)/len(self.tempfile)*100,1])


class AbfConvert(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(AbfConvert, self).__init__(parent)
        self.setupUi(self)
        self.files=[]
        self.actionOpen.triggered.connect(self.openfile)
        self.actionOpenFolder.triggered.connect(self.openfolder)
        self.actionClearAllFiles.triggered.connect(self.clearlist)
        self.RunButton.clicked.connect(self.runconvert)
        self.actionExit.triggered.connect(self.closeEvent)
        self.actionaboutmenu.triggered.connect(self.about)
    def openfile(self):
        self.statusBar().showMessage(self.tr("Open file"))
        fn = QFileDialog.getOpenFileNames(self, self.tr(
            "Open file"), filter='Abf Files (*.abf)')
        if len(fn[0]) == 0:
            self.statusBar().showMessage(self.tr("No file selected"))
        else:
            for i in fn[0]:
                if i not in self.files:
                    self.files.append(i)
                    self.listWidget.addItem(os.path.basename(i))
    
    def openfolder(self):
        self.statusBar().showMessage(self.tr("Open folder"))
        fn = QFileDialog.getExistingDirectory(self,
                  "选取文件夹",
                  "./")
        files=glob.glob(fn+'/*.abf')
        for i in files:
            i=i.replace('\\','/')
            if i not in self.files:
                self.files.append(i)
                self.listWidget.addItem(os.path.basename(i))
    
    def clearlist(self):
        self.files=[]
        self.listWidget.clear()

    def runconvert(self):
        if self.files:
            tempfile=[]
            s = self.listWidget.selectedIndexes()
            if s:
                for i in s:
                    tempfile.append(self.files[i.row()])
            else:
                tempfile=self.files
            if self.comboBox_aimfile.currentIndex() == 0:
                # convert to matlab .mat file
                for index,j in enumerate(tempfile):
                    temp=Convert(j)
                    temp.toMat()
                    self.progressBar.setValue((index+1)/len(tempfile)*100)
                QMessageBox.information(self, self.tr("Errors"), self.tr(
                        "文件转换完成"), QMessageBox.Ok)
                self.progressBar.setValue(0)
            elif self.comboBox_aimfile.currentIndex() == 3:
                # convert to matlab .mat file
                for index,j in enumerate(tempfile):
                    temp=Convert(j)
                    temp.toTdms()
                    self.progressBar.setValue((index+1)/len(tempfile)*100)
                QMessageBox.information(self, self.tr("Errors"), self.tr(
                        "文件转换完成"), QMessageBox.Ok)
                self.progressBar.setValue(0)
            else:
                if self.comboBox_aimfile.currentIndex() == 1:
                    suffix='csv'
                else:
                    suffix='txt'
                self.convert=Worker(tempfile,suffix,self.isSplitCheck.isChecked(),self.spinBox_timestep.value())
                self.convert.progressBarValue.connect(self.setProgress)
                self.convert.start()    
                self.listWidget.setEnabled(False)
                self.RunButton.setEnabled(False)
        else:
            QMessageBox.information(self, self.tr("Errors"), self.tr(
                    "No files are ready converted"), QMessageBox.Ok)

    def setProgress(self,perc):
        self.progressBar.setValue(perc[0])
        if perc[1]==1:
            QMessageBox.information(self, self.tr("Errors"), self.tr(
                        "文件转换完成"), QMessageBox.Ok)
            self.listWidget.setEnabled(True)
            self.RunButton.setEnabled(True)

    def closeEvent(self,event):
        sys.exit(app.exec_())
        
    def about(self):
        self.about_dia=Ui_Dialog()
        self.Dialog_d = QDialog(self)
        self.about_dia.setupUi(self.Dialog_d)
        self.about_dia.pushButton.clicked.connect(self.about_close)
        self.Dialog_d.exec_()

    def about_close(self):
        self.Dialog_d.close()
        


        


if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = AbfConvert()
    mainWindow.show()
    sys.exit(app.exec_())