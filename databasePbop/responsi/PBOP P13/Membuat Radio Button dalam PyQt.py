# Membuat Radio Button

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def _init_(self):
        super()._init_()
        self.setupUi()

    def setupUi(self):
        self.resize(300,100)
        self.setWindowTitle('Demo QRadioButton')

        self.label=QLabel('Jenis Kelamin :')
        self.radio1=QRadioButton('Laki-laki')
        self.radio2=QRadioButton('Perempuan')
        self.okButton=QPushButton('OK')

        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.okButton)

        self.setLayout(vbox)
        self.okButton.clicked.connect(self.on_okButton_clicked)

    def on_okButton_clicked(self):
        if self.radio1.isChecked():
            gender=self.radio1.text()
        elif self.radio1.isChecked():
            gender=self.radio1.text()
        else:
            gender=None

        if gender==None:
            QMessageBox.information(self,'Informasi','Anda belum memilih opsi')
        else:
            QMessageBox.information(self,'Informasi','Anda memilih "%s"' % gender)

if __name__ == '__main__':
    a=QApplication(sys.argv)
    form=MainForm()
    form.show()
    a.exec_()