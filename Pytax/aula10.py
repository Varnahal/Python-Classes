from PySide6.QtWidgets import QApplication,QMainWindow, QLineEdit
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")

        self.inp = QLineEdit()
        self.inp.setMaxLength(10)
        self.inp.setPlaceholderText('Digite seu nome')
        self.inp.returnPressed.connect(self.return_pressed)
        self.inp.selectionChanged.connect(self.selection_changed)
        self.inp.textEdited.connect(self.text_edited)
        self.inp.textChanged.connect(self.text_changed)
        self.inp.setInputMask('000.000.000-00;_')
        self.setCentralWidget(self.inp)


    def return_pressed(self):
        print('button pressed!!')
        self.inp.setMaxLength(15)
        self.centralWidget().setText(f'Olá, {self.inp.text()}')

    
    def selection_changed(self):
        print('Texto selecionado ...')

    
    def text_edited(self,s):
        print('Texto editado ...')
        print(s)


    def text_changed(self,s):
        print('Texto alterado ...')
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()