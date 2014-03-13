#https://github.com/Hausaufgaben/GitHubVS2013.git
#https://github.com/SmAaMyA/GitHubVS2013---test.git

import sys
from PySide.QtGui import *
from PySide.QtCore import *

''' No.1
class Simple_drawing_window(QWidget):
	def __init__ (self):
		QWidget.__init__(self, None)
		self.setWindowTitle("Simple Drawing")
		self.rabbit = QImage("images/rabbit.png")

	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)

		p.setPen(QColor(0, 0, 0))
		p.setBrush(QColor(0, 127, 0))
		p.drawPolygon([QPoint(70, 100), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150)])
		p.setPen(QColor(255, 127, 0))
		p.setBrush(QColor(255, 127, 0))
		p.drawPie(50, 150, 100, 100, 0, 180 * 16)

		p.drawPolygon([QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)])

		p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
		p.end()

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
'''

''' No. 2
class Self_simple_drawing(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500, 500)

        self.stage = QImage(QSize(500, 500), QImage.Format_RGB32)
        self.stage.fill(QColor(255, 255, 255))
        self.beginPoint = QPoint()

    def paintEvent(self, event):
        p = QPainter(self)
        p.drawImage(event.rect(), self.stage)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.beginPoint = event.pos()
            self.pressed = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.pressed:
            self.drawing(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.pressed:
            self.drawing(event.pos())
            self.pressed = False

    def drawing(self, endPoint):
        p = QPainter(self.stage)
        p.setPen(QPen(QColor(0, 0, 0), 5))
        p.drawLine(self.beginPoint, endPoint)

        self.update()
        self.beginPoint = QPoint(endPoint)

    def clearScreen(self):
        self.stage.fill(QColor(255, 255, 255))
        self.update()

class Simple_paint(QWidget):
    def __init__ (self):
        QWidget.__init__(self)
        self.setWindowTitle("Self Simple Drawing")
        #self.setFixedSize(500,550)
        
        self.program = Self_simple_drawing()
        clearButton = QPushButton("Clear")
        clearButton.clicked.connect(self.clearActions)
        label = QLabel("<p align=\"center\">Drag the mouse to draw</p>")

        layout = QVBoxLayout()
        layout.addWidget(self.program)
        layout.addWidget(label)
        layout.addWidget(clearButton)
        self.setLayout(layout)

    def clearActions(self):
        self.program.clearScreen()
'''

def main():
    app = QApplication(sys.argv);

    w = Simple_paint()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())