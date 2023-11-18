from PySide6.QtWidgets import QApplication,QMainWindow,QSlider
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aula12')
        slider = QSlider()
        slider.setMinimum(-10)
        slider.setMaximum(10)
        slider.setSingleStep(3)

        slider.valueChanged.connect(self.value_Change)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(slider)


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