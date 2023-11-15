from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
import sys

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("José é gay")
        ck = QCheckBox("Marque aki")
        ck.setChecked(True)
        ck.stateChanged.connect(self.show_state)
        self.setCentralWidget(ck)


    def show_state(self,s):
        print(s == 2)
        print(s)


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()