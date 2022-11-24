from random import randint
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_repaint = 0
        self.draw.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.do_repaint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_repaint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            w = randint(0, 500)
            x = randint(0, self.width() - w)
            y = randint(0, self.height() - w)
            qp.drawEllipse(max(0, x), max(0, y), w, w)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())