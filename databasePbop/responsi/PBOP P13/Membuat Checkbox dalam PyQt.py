# Membuat Checkbox

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def _init_(self):
        super()._init_()
        self.setupUi()

    def setupUi(self):
        self.resize(250,100)
        self.setWindowTitle('Demo QCheckButton')

        self.label=QLabel('Bahasa pemrograman yang dikuasai :')
        self.checkbox1=QCheckBox('Python')
        self.checkbox2=QCheckBox('PHP')
        self.checkbox3=QCheckBox('Java')
        self.checkbox4=QCheckBox('C++')
        self.okButton=QPushButton('OK')

        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.checkbox1)
        vbox.addWidget(self.checkbox2)
        vbox.addWidget(self.checkbox3)
        vbox.addWidget(self.checkbox4)
        vbox.addWidget(self.okButton)

        self.setLayout(vbox)
        self.okButton.clicked.connect(self.on_okButton_clicked)

    def on_okButton_clicked(self):
        lang=[]
        if self.checkbox1.isChecked(): lang.append('Python')
        if self.checkbox2.isChecked(): lang.append('PHP')
        if self.checkbox3.isChecked(): lang.append('Java')
        if self.checkbox4.isChecked(): lang.append('C++')

        QMessageBox.information(self,'Informasi','Anda memilih "%s"' % str(lang))

if __name__ == '__main__':
    a=QApplication(sys.argv)
    form=MainForm()
    form.show()
    a.exec_()