from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import sys


class GUI(QWidget):

    # Window Reqs
    WINDOW_X_LOC = 500
    WINDOW_Y_LOC = 500
    WINDOW_WIDTH = 1500
    WINDOW_HEIGHT = 800

    # Import Button Locs
    IMPORT_BTN_X = WINDOW_X_LOC/5
    IMPORT_BTN_Y = WINDOW_Y_LOC
    IMPORT_BTN_WIDTH = 80
    IMPORT_BTN_HEIGHT = 40

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(self.WINDOW_X_LOC, self.WINDOW_Y_LOC, self.WINDOW_WIDTH, self.WINDOW_HEIGHT) #(x,y, width, height)
        self.setWindowTitle('PYDJ')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.createButton(self.IMPORT_BTN_X, self.IMPORT_BTN_Y, self.IMPORT_BTN_WIDTH, self.IMPORT_BTN_HEIGHT, 'IMPORT')
        self.show()

    def createButton(self, x, y, width, height, title):
        button = QPushButton(title, self)
        button.clicked.connect(QApplication.instance().quit)
        button.resize(width, height)
        button.move(x,y)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())