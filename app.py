import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Миноискатель')
        self.gl = QGridLayout(9, 9)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
