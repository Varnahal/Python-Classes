from PySide6.QtWidgets import QApplication,QMainWindow,QDial
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aula12')
        dial = QDial()
        dial.setRange(-10,10)
        dial.setSingleStep(0.5)
        dial.valueChanged.connect(self.value_Change)
        dial.sliderMoved.connect(self.slider_position)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(dial)


    def value_Change(self, i):
        print(i)
    

    def slider_position(self,p):
        print(f'position: {p}')

    
    def slider_pressed(self):
        print('pressed')
    

    def slider_released(self):
        print('released')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()