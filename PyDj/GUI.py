from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import sys

class MainWindow(QMainWindow):

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
        self.createMenu()
        self.show()


    def createButton(self, x, y, width, height, title):
        button = QPushButton(title, self)
        button.clicked.connect(QApplication.instance().quit)
        button.resize(width, height)
        button.move(x,y)


    def createMenu(self):
        newAction = QAction(QIcon('new.png'), '&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New File')
        newAction.triggered.connect(self.newCall)

        openAction = QAction(QIcon('open.jpg'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.openCall)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit File')
        exitAction.triggered.connect(self.exitCall)       

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)






    def newCall(self):
        print("New")

    def openCall(self):
        print("Open")

    def exitCall(self):
        sys.exit(app.exec_())
    

    

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())