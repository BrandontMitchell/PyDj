from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import sys
import os

class MainWindow(QMainWindow):

    # Window Reqs
    WINDOW_X_LOC = 500
    WINDOW_Y_LOC = 500
    WINDOW_WIDTH = 1500
    WINDOW_HEIGHT = 800

    # Song description text locs
    SONG_DESC_X = WINDOW_X_LOC/5
    SONG_DESC_Y = WINDOW_Y_LOC/5
    SONG_DESC_WIDTH = 80
    SONG_DISC_HEIGHT = 40


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
        self.createTextBox(self.SONG_DESC_X, self.SONG_DESC_Y, self.SONG_DESC_WIDTH, self.SONG_DISC_HEIGHT, "ARTIST")
        self.show()

    def createMenu(self):
        new_icon = os.path.join("Assets", "new.png") 
        newAction = QAction(QIcon(new_icon), '&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New File')
        newAction.triggered.connect(self.newCall)

        open_icon = os.path.join("Assets", "open.png") 
        openAction = QAction(QIcon(open_icon), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.openCall)

        exit_icon = os.path.join("Assets", "exit.png") 
        exitAction = QAction(QIcon(exit_icon), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit File')
        exitAction.triggered.connect(self.exitCall)       

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)


    def createButton(self, x, y, width, height, title):
        button = QPushButton(title, self)
        button.clicked.connect(QApplication.instance().quit)
        button.resize(width, height)
        button.move(x,y)

    def createTextBox(self, x, y, width, height, title):
        self.nameLabel = QLabel(self)
        self.nameLabel.setText(title)
        self.line = QLineEdit(self)

        self.line.move(x,y)
        self.line.resize(width,height)
        self.nameLabel.move(x-100,y)

    






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