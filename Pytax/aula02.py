from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")

        self.button = QPushButton("CLIQUE AQUI")

        self.setFixedSize(QSize(300,400))
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clicked_button)
    

    def clicked_button(self):
        print("Botão apertado")
        self.button.setEnabled(False)
        self.setWindowTitle("Why?")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()