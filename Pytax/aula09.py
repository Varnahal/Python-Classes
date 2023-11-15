from PySide6.QtWidgets import QApplication,QMainWindow,QListWidget
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(300,400))
        lb = QListWidget()
        lb.addItems(['penio','jooj','varnahal','roberto'])
        lb.currentItemChanged.connect(self.index_changed)
        lb.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(lb)


    def index_changed(self,i):
        print(i.text())


    def text_changed(self,s):
        print(s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()