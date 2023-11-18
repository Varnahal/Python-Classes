from PySide6.QtWidgets import QApplication,QMainWindow, QVBoxLayout,QWidget
from PySide6.QtCore import QSize
import sys

from layout_color import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('black'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('orange'))
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()