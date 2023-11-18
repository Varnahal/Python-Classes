from PySide6.QtWidgets import QApplication,QMainWindow, QVBoxLayout,QFrame,QLineEdit,QPushButton
import pyshorteners
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Short link')
        self.resize(400,300)
        layout = QVBoxLayout()
        self.frame = QFrame()
        self.link = QLineEdit(self.frame)
        self.link.setPlaceholderText("Coloque seu link aqui")

        self.btn = QPushButton(self.frame)
        self.btn.setText("Executar")

        self.result = QLineEdit(self.frame)

        layout.addWidget(self.link)
        layout.addWidget(self.btn)
        layout.addWidget(self.result)

        self.frame.setLayout(layout)

        self.btn.pressed.connect(self.link_shortener)

        self.setCentralWidget(self.frame)


    def link_shortener(self):
        short = pyshorteners.Shortener()
        new_link = short.tinyurl.short(self.link.text())
        self.result.setText(new_link)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()