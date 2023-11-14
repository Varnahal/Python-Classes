from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
import sys

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("José é gay")
        ck = QCheckBox("Marque aki")
        ck.setChecked(True)
        self.setCentralWidget(ck)


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()