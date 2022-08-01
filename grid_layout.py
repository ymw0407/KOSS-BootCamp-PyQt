import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.des()
        self.form()

        grid.addWidget(self.titleDes, 0, 0)
        grid.addWidget(self.authorDes, 1, 0)
        grid.addWidget(self.textDes, 2, 0)

        grid.addWidget(self.titleForm, 0, 1)
        grid.addWidget(self.authorForm, 1, 1)
        grid.addWidget(self.textForm, 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def des(self):
        self.titleDes = QLabel("Title:")
        self.authorDes = QLabel("Author:")
        self.textDes = QLabel("Review:")

    def form(self):
        self.titleForm = QLineEdit()
        self.authorForm = QLineEdit()
        self.textForm = QTextEdit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())