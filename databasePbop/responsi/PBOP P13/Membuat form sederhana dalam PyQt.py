# Membuat Program GUI dalam PyQt

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__=='__main__':
    a = QApplication(sys.argv)

    form=QWidget()
    form.setGeometry(100,150,350,250)
    form.setWindowTitle('Program GUI dalam PyQt')

    label=QLabel()
    label.setText('Halo Teman, Bagaimana kabarmu?')
    label.move(140,100)
    label.setParent(form)

    form.show()
    a.exec_()