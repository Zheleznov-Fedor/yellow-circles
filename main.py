from random import randint
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_repaint = 0
        self.draw.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.do_repaint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_repaint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            w = randint(0, 500)
            x = randint(0, self.width())
            y = randint(0, self.height())
            qp.drawEllipse(max(0, x - w // 2), max(0, y - w // 2), w, w)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())