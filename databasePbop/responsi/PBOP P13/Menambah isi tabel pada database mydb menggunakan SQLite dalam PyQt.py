# Insert data SQLite melalui PyQt

# from PyQt import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
import sys
import sqlite3

class MainForm(QWidget):
    def _init_(self):
        super()._init_()
        self.setupUi()

    def setupUi(self):
        self.resize(250,100)
        self.setWindowTitle('Insert Data Produk')

        self.label1=QLabel('Kode')
        self.kodeEdit=QLineEdit()
        self.label2=QLabel('Nama')
        self.namaEdit=QLineEdit()
        self.label3=QLabel('Harga')
        self.hargaEdit=QLineEdit()
        self.saveButton=QPushButton('Save')
        self.clearButton=QPushButton('Clear')
        self.exitButton=QPushButton('Exit')

        grid=QGridLayout()
        grid.addWidget(self.label1,0,0)
        grid.addWidget(self.kodeEdit,0,1,1,2)
        grid.addWidget(self.label2,1,0)
        grid.addWidget(self.namaEdit,1,1,1,2)
        grid.addWidget(self.label3,2,0)
        grid.addWidget(self.hargaEdit,2,1,1,2)
        grid.addWidget(self.saveButton,3,1)
        grid.addWidget(self.clearButton,3,2)
        grid.addWidget(self.exitButton,3,3)

        self.setLayout(grid)
        self.saveButton.clicked.connect(self.insert_data)
        self.clearButton.clicked.connect(self.on_clearButton_clicked)
        self.exitButton.clicked.connect(self.on_exitButton_clicked)

    def on_clearButton_clicked(self):
        self.kodeEdit.clear()
        self.namaEdit.clear()
        self.hargaEdit.clear()

    def on_exitButton_clicked(self):
        self.close

    def insert_data(self):
        try:
            conn = sqlite3.connect("pbop13")
            cur = conn.cursor()

            kode = self.kodeEdit.text()
            nama = self.namaEdit.text()
            harga = self.hargaEdit.text()

            data_produk=[kode, nama, harga]
            cur.execute("INSERT INTO produk (kode, nama, harga) VALUES (?, ?, ?)", data_produk)

            conn.commit()
            conn.close()
            print('Data Berhasil Disimpan')
        except conn.Error as e:
            print('Data Berhasil Disimpan')

if __name__ == '__main__':
    a=QApplication(sys.argv)
    form=MainForm()
    form.show()
    a.exec_()