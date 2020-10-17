import sys
from PyQt5 import QtWidgets

## PyQtの環境はQtを直接入れた方がよい

app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel("Hello")
label.show()
app.exec_()