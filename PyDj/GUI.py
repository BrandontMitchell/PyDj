from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QPushButton, QAction, QSizePolicy, QLineEdit, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt 
import numpy
import random 
import librosa
import librosa.display
import sys
import os

class MainWindow(QMainWindow):

    # Window Reqs
    WINDOW_X_LOC = 500
    WINDOW_Y_LOC = 500
    WINDOW_WIDTH = 1500
    WINDOW_HEIGHT = 800

    # Song description text locs
    SONG_DESC_X = 100
    SONG_DESC_Y = 150
    SONG_DESC_WIDTH = 80
    SONG_DISC_HEIGHT = 30
    ARTIST_DESC_X = 100
    ARTIST_DESC_Y = 75


    # Import Button Locs
    IMPORT_BTN_X = 100
    IMPORT_BTN_Y = 225
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
        self.createArtistTextBox(self.SONG_DESC_X, self.SONG_DESC_Y, self.SONG_DESC_WIDTH, self.SONG_DISC_HEIGHT, "Artist")
        self.createSongTextBox(self.ARTIST_DESC_X, self.ARTIST_DESC_Y, self.SONG_DESC_WIDTH, self.SONG_DISC_HEIGHT, "Song Title")
        # m = PlotCanvas(self, width=5, height=4)
        # m.move(200, 200)
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
        button.clicked.connect(self.getTitle)
        button.clicked.connect(self.openFile)
        button.resize(width, height)
        button.move(x,y)

    def createArtistTextBox(self, x, y, width, height, title):
        self.nameLabel = QLabel(self)
        self.nameLabel.setText(title)
        self.artistLine = QLineEdit(self)

        self.artistLine.move(x,y)
        self.artistLine.resize(width,height)
        self.nameLabel.move(x-85,y)

    def createSongTextBox(self, x, y, width, height, title):
        self.songLabel = QLabel(self)
        self.songLabel.setText(title)
        self.songLine = QLineEdit(self)

        self.songLine.move(x,y)
        self.songLine.resize(width,height)
        self.songLabel.move(x-85,y)
        

    def openFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        y, sr = librosa.load(name[0])
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        print('Estimated temp: {:.2f} beats per minute'.format(tempo))


    def getAudioInput(self):
        testFileOne = os.path.join("Audio Files", "test1.wav") 


    def getTitle(self):
        artist = self.artistLine.text()
        song = self.songLine.text()
        print(f'Artist: {artist}')
        print(f'Song: {song}')


    





    def newCall(self):
        print("New")

    def openCall(self):
        print("Open")

    def exitCall(self):
        sys.exit(app.exec_())
    

    
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize = (width, height), dpi=dpi)
        self.axes=fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, 
                    QSizePolicy.Expanding,
                    QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)
        thinkplot.config(xlabel="time", legend=False)
        wave = sin_sig.make_wave(duration=1, framerate=11025)
        wave.plot()
        thinkplot.show()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())