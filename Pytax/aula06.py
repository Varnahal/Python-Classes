from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from PySide6.QtGui import QPixmap

import sys

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Pixel")


        widget = QLabel('Pixel')
        widget.setScaledContents(True)
        widget.setPixmap(QPixmap(r"C:\Users\danie\Documents\GitHub\Python-Classes\Pytax\fotoaleatoria.jpeg"))

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()
