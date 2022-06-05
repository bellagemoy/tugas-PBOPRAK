# Menampilkan dialog pesan

import sys
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(350,100)
        self.setWindowTitle('Demo QMessageBox')
        self.informationButton=QPushButton('Informasi')
        self.errorButton=QPushButton('Kesalahan')
        self.warningButton=QPushButton('Peringatan')
        self.confirmButton=QPushButton('Konfirmasi')

        hbox=QHBoxLayout()
        hbox.addWidget(self.informationButton)
        hbox.addWidget(self.errorButton)
        hbox.addWidget(self.warningButton)
        hbox.addWidget(self.confirmButton)

        self.setLayout(hbox)
        self.informationButton.clicked.connect(self.on_informationButton_clicked)
        self.errorButton.clicked.connect(self.on_errorButton_clicked)
        self.warningButton.clicked.connect(self.on_warningButton_clicked)
        self.confirmButton.clicked.connect(self.on_confirmButton_clicked)

    def on_informationButton_clicked(self):
        QMessageBox.information(self,'Informasi','Data telah tersimpan di database')

    def on_errorButton_clicked(self):
        QMessageBox.critical(self,'Kesalahan','File config.ini tidak ditemukan')

    def on_warningButton_clicked(self):
        QMessageBox.warning(self,'Peringatan','Semua data dalam flashdisk akan dihapus !')

    def on_confirmButton_clicked(self):
        dialog=QMessageBox.question(self,'Konfirmasi','Hapus baris data ini ?')

        if dialog==QMessageBox.Yes:
            print('Anda memilih YES')
        else:
            print('Anda memilih NO')

if __name__=='__main__':
    a=QApplication(sys.argv)
    form=MainForm()
    form.show()
    a.exec_()