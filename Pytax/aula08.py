from PySide6.QtWidgets import QApplication,QMainWindow,QComboBox
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(300,400))
        self.widget = QComboBox()
        self.widget.addItems(['penio','jooj','varnahal','roberto'])
        self.widget.currentIndexChanged.connect(self.index_change)
        self.widget.currentTextChanged.connect(self.text_change)
        self.setCentralWidget(self.widget)


    def index_change(self,i):
        print(i)


    def text_change(self,s):
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()