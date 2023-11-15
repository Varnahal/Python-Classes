from PySide6.QtWidgets import QApplication,QMainWindow, QSpinBox,QDoubleSpinBox
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")

        #self.spin = QSpinBox()
        self.spin = QDoubleSpinBox()
        self.spin.setMinimum(-5)
        self.spin.setMaximum(5)
        self.spin.setSuffix(' BCT')
        self.spin.valueChanged.connect(self.showValue)
        self.spin.textChanged.connect(self.showText)

        self.setCentralWidget(self.spin)
    

    def showValue(self,i):
        print(i)


    def showText(self,s):
        print(s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()