import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QGridLayout, QLCDNumber, QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtGui import (QFont, QPalette, QColor)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.cols = 15
        self.rows = 9
        self.bombs = 10
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 180, 180)
        self.setWindowTitle('Миноискатель')
        self.remain_indicator = QLCDNumber()
        self.remain_indicator.setStyleSheet("""QLCDNumber { 
                                               background-color: black; 
                                               color: red; }""")
        self.remain_indicator.setSegmentStyle(QLCDNumber.Flat)
        self.remain_indicator.setFixedSize(80, 35)
        self.remain_indicator.display(self.bombs)
        self.new_game_button = QPushButton()
        self.new_game_button.setFont(QFont('Times', 11))
        self.new_game_button.setText('🙂')  # 😎 😟
        self.new_game_button.setFixedSize(35, 35)
        self.time_indicator = QLCDNumber()
        self.time_indicator.setSegmentStyle(QLCDNumber.Flat)
        self.time_indicator.setStyleSheet("""QLCDNumber { 
                                           background-color: black; 
                                           color: red; }""")
        self.time_indicator.setFixedSize(80, 35)
        self.time_indicator.display(0)
        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.remain_indicator)
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.new_game_button, 1)
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.time_indicator, 1)
        self.gl = QGridLayout()
        self.field_buttons = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                cell_button = QPushButton()
                cell_button.setFixedSize(20, 20)  # 🚩 💣 💥
                row.append(cell_button)
                self.gl.addWidget(cell_button, i, j)
            self.field_buttons.append(row)
        # for i in range
        # for  in zip(positions, names):
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     self.gl.addWidget(button, *position)
        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.gl)
        self.v_box.addStretch()
        self.setLayout(self.v_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
