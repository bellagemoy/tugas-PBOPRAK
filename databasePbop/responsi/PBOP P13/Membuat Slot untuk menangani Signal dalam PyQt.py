# Membuat Slot untuk menangani Signal

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250,100)
        self.setWindowTitle('Demo Signal dan Slot')

        self.label=QLabel('Masukkan Nama Anda')
        self.nameEdit=QLineEdit()
        self.haloButton=QPushButton('Halo')

        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.nameEdit)
        vbox.addWidget(self.haloButton)

        self.setLayout(vbox)
        self.haloButton.clicked.connect(self.on_haloButton_clicked)

    def on_haloButton_clicked(self):
        name=self.nameEdit.text()
        QMessageBox.information(self,'Halo','Hai %s, apa kabar?' % name)

if __name__=='__main__':
    a=QApplication(sys.argv)
    form=MainForm()
    form.show()
    a.exec_()