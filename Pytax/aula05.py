from typing import Optional
from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
import sys


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Aula05')
        widget = QLabel("Aula 05 - Label")
        font = widget.font()
        font.setPointSize(35)
        widget.setFont(font)

        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()