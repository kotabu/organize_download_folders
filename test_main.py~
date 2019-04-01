import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from untitled import Ui_MainWindow
from dialog import Ui_Dialog
from test import MainScript

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)

        self.dialog.pushButton.clicked.connect(self.dialog_close)

    def dialog_close(self):
        self.close()

    def dialog_change(self,text):
        self.dialog.label.setText(text)


class App(QMainWindow):
    def __init__(self,parent=None):
        super(App, self).__init__(parent)
        self.download_path = ""
        self.zip = 0
        self.rar = 0
        self.z7 = 0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.start_click)
        self.ui.pushButton_2.clicked.connect(qApp.quit)
        self.ui.pushButton_3.clicked.connect(self.browse_click)
        self.ui.checkBox.stateChanged.connect(self.file_extension)
        self.ui.checkBox_2.stateChanged.connect(self.file_extension)
        self.ui.checkBox_3.stateChanged.connect(self.file_extension)


    def start_click(self):
        if self.download_path != "":
            main = MainScript()
            main.main(self.download_path,self.zip,self.rar,self.z7)
            dlg = Dialog()
            dlg.dialog_change("Processing completed")
            dlg.show()
            dlg.exec_()
        else:
            dlg = Dialog()
            dlg.dialog_change("Please specify the download folder path")
            dlg.show()
            dlg.exec_() 

    def browse_click(self):
        path = str(QFileDialog.getExistingDirectory(self,"Select Directory"))
        self.ui.lineEdit.setText(path)
        self.download_path = self.ui.lineEdit.text()

    def file_extension(self):
        if self.ui.checkBox.isChecked():
            self.zip = 1
        else:
            self.zip = 0

        if self.ui.checkBox_2.isChecked():
            self.rar = 1
        else:
            self.rar = 0
        
        if self.ui.checkBox_3.isChecked():
            self.z7 = 1
        else:
            self.z7 = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

