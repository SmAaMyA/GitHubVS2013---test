import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 1")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(400, 50), QPoint(200, 250), QPoint(600, 250)])

        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 2")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPie(50, 50, 200, 200, 0, 360 * 16)

        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 3")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 128))
        p.drawPolygon([QPoint(200, 50), QPoint(200, 250), QPoint(600, 250), QPoint(450,50)])
        p.end()

def main():
    app = QApplication(sys.argv)

    w1 = Simple_drawing_window1()
    w1.show()
    w2 = Simple_drawing_window2()
    w2.show()
    w3 = Simple_drawing_window3()
    w3.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())