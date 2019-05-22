from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QVBoxLayout, QPushButton, QAction, QSizePolicy, QLineEdit, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt 
import numpy as np
import random 
import librosa
import librosa.display
import sys
import os

class MainWindow(QMainWindow):

    # Window Reqs
    WINDOW_X_LOC = 500
    WINDOW_Y_LOC = 500
    WINDOW_WIDTH = 1800
    WINDOW_HEIGHT = 1000

    # Song description text locs
    SONG_DESC_X = 100
    SONG_DESC_Y = 150
    SONG_DESC_WIDTH = 80
    SONG_DISC_HEIGHT = 30
    ARTIST_DESC_X = 100
    ARTIST_DESC_Y = 75
    SUMMARY_DESC_X = 25

    # Import Button Locs
    IMPORT_BTN_X = 100
    IMPORT_BTN_Y = 225
    IMPORT_BTN_WIDTH = 80
    IMPORT_BTN_HEIGHT = 40

    # Graph Locs
    GRAPH_BG_WIDTH = 700
    GRAPH_BG_HEIGHT = 400
    GRAPH_WIDTH = 645
    GRAPH_HEIGHT = 335

    FREQ_GRAPH_X = 330
    FREQ_GRAPH_BG_X = 300
    FREQ_GRAPH_Y = 95
    FREQ_GRAPH_BG_Y = 40
    
    PITCH_GRAPH_X = 1040
    PITCH_GRAPH_BG_X = 1010
    PITCH_GRAPH_Y = 95
    PITCH_GRAPH_BG_Y = 40 

    BEAT_GRAPH_X = 330
    BEAT_GRAPH_BG_X = 300
    BEAT_GRAPH_Y = 505
    BEAT_GRAPH_BG_Y = 450

    MFCC_GRAPH_X = 1040
    MFCC_GRAPH_BG_X = 1010
    MFCC_GRAPH_Y = 505
    MFCC_GRAPH_BG_Y = 450

    inputDetected = False
    bpm = 0
    maxFreq = 0

    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.graphBackground(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, 'backwindow.jpg')
        self.setGeometry(self.WINDOW_X_LOC, self.WINDOW_Y_LOC, self.WINDOW_WIDTH, self.WINDOW_HEIGHT) #(x,y, width, height)
        self.setWindowTitle('PYDJ')
        self.setWindowIcon(QIcon(os.path.join("Assets", "icon.jpg")))
        self.createMenu()

        self.createButton(self.IMPORT_BTN_X, self.IMPORT_BTN_Y, self.IMPORT_BTN_WIDTH, self.IMPORT_BTN_HEIGHT, 'IMPORT')
        self.createArtistTextBox(self.SONG_DESC_X, self.SONG_DESC_Y, self.SONG_DESC_WIDTH, self.SONG_DISC_HEIGHT, "Artist")
        self.createSongTextBox(self.ARTIST_DESC_X, self.ARTIST_DESC_Y, self.SONG_DESC_WIDTH, self.SONG_DISC_HEIGHT, "Song Title")
        
        self.graphBackground(self.FREQ_GRAPH_BG_X-10, self.FREQ_GRAPH_BG_Y-10, 2.04*self.GRAPH_BG_WIDTH, 2.08*self.GRAPH_BG_HEIGHT, 'backbg.png')
        self.graphBackground(self.FREQ_GRAPH_BG_X, self.FREQ_GRAPH_BG_Y, self.GRAPH_BG_WIDTH, self.GRAPH_BG_HEIGHT, 'bgf.jpg')
        self.graphBackground(self.PITCH_GRAPH_BG_X, self.PITCH_GRAPH_BG_Y, self.GRAPH_BG_WIDTH, self.GRAPH_BG_HEIGHT, 'bgf.jpg')
        self.graphBackground(self.BEAT_GRAPH_BG_X, self.BEAT_GRAPH_BG_Y, self.GRAPH_BG_WIDTH, self.GRAPH_BG_HEIGHT, 'bgf.jpg')
        self.graphBackground(self.MFCC_GRAPH_BG_X, self.MFCC_GRAPH_BG_Y, self.GRAPH_BG_WIDTH, self.GRAPH_BG_HEIGHT, 'bgf.jpg')
        self.graphBackground(self.SUMMARY_DESC_X-15, self.IMPORT_BTN_Y+75, self.GRAPH_BG_WIDTH/2.6, 1.4*self.GRAPH_BG_HEIGHT, 'summarybg.jpg')

        self.createSummary(self.SUMMARY_DESC_X, self.IMPORT_BTN_Y+75, "---  BREAKDOWN  ---")
        self.createBPM(self.SUMMARY_DESC_X, self.IMPORT_BTN_Y+150, "BPM: " + str(self.bpm))
        self.createFREQ(self.SUMMARY_DESC_X, self.IMPORT_BTN_Y+225, "Max Freq: " + str(self.maxFreq))

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
        
    def createSummary(self, x, y, text):
        self.summaryLabel = QLabel(self)
        self.summaryLabel.setText(text)
        self.summaryLabel.move(x, y)

    def createBPM(self, x, y, text):
        self.bpmLabel = QLabel(self)
        self.bpmLabel.setText(text)
        self.bpmLabel.move(x, y)

    def createFREQ(self, x, y, text):
        self.freqLabel = QLabel(self)
        self.freqLabel.setText(text)
        self.freqLabel.move(x, y)

    def openFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        self.getAudioMetrics(name[0])


    def graphBackground(self, x, y, width, height, image):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(os.path.join("Assets", image)))
        self.label.setGeometry(x, y, width, height)
        

##################      ANALYSIS     ##################
    
    def getTitle(self):
        artist = self.artistLine.text()
        song = self.songLine.text()
        print(f'Artist: {artist}')
        print(f'Song: {song}')


    def getAudioMetrics(self, filename):
        y, sr = librosa.load(filename)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        genre = ''
        genreDict = {
            'R&B/Slow': range(0,65),
            'Hip Hop': range(65, 115),
            'House': range(115, 130),
            'Techno/EDM': range(130, 140),
            'Dubstep': range(140, 160),
            'Hardcore': range(160, 300)
        }
        print("Beats frames" + str(beat_frames))
        # loops through genre dictionary to match bpm from input file
        # to a specific genre, helpful when mixing
        for key, value in genreDict.items():
            if int(tempo) in value:
                genre = key

        print('Estimated temp: {:.2f} beats per minute'.format(tempo))
        print()
        print(f'This falls under {genre} music')

        
        self.displayFreqGraph(y, sr, self.FREQ_GRAPH_X, self.FREQ_GRAPH_Y)
        self.displayPitchGraph(y, sr, self.PITCH_GRAPH_X, self.PITCH_GRAPH_Y)
        self.displayBeatGraph(y, sr, self.BEAT_GRAPH_X, self.BEAT_GRAPH_Y)
        self.displayMFCCGraph(y, sr, self.MFCC_GRAPH_X, self.MFCC_GRAPH_Y)

        self.bpmLabel.setText("BPM: " + str(tempo))
        self.freqLabel.setText("Max Freq: " + str(self.maxFreq))
        

    def displayFreqGraph(self, arr, samplerate, x, y):
        librosa.display.waveplot(arr, sr=samplerate)
        self.maxFreq = arr.max()
        
        plt.title("Freq Detection")
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(x+self.WINDOW_X_LOC, y + self.WINDOW_Y_LOC, self.GRAPH_WIDTH, self.GRAPH_HEIGHT)
        plt.tight_layout()
        plt.show()
        
    def displayPitchGraph(self, arr, int, x, y):
        y_harmonic, y_percussive = librosa.effects.hpss(arr)
        C = librosa.feature.chroma_cqt(y=y_harmonic, sr=int)

        plt.figure(figsize=(12,4), num="Pitch Graph")
        librosa.display.specshow(C, sr=int, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
        
        plt.title("Pitch Detection - Chromagram")
        plt.colorbar()
        
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(x+self.WINDOW_X_LOC, y + self.WINDOW_Y_LOC, self.GRAPH_WIDTH, self.GRAPH_HEIGHT)
        plt.tight_layout()
        plt.show()
        
    def displayBeatGraph(self, arr, int, x, y):
        y_harmonic, y_percussive = librosa.effects.hpss(arr)
        S = librosa.feature.melspectrogram(arr, sr=int, n_mels=128)
        log_S = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(12,4), num="Beat Graph")
        tempo, beats = librosa.beat.beat_track(y=y_percussive, sr=int)
        librosa.display.specshow(log_S, sr=int, x_axis='time', y_axis='mel', alpha=0.8)

        plt.vlines(librosa.frames_to_time(beats),
                    1, 0.5*int,
                    colors='r', linestyles='-', linewidth=5, alpha=0.5)
        plt.axis('tight')
        plt.colorbar(format='%+02.0f dB')

        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(x+self.WINDOW_X_LOC, y + self.WINDOW_Y_LOC, self.GRAPH_WIDTH, self.GRAPH_HEIGHT)
        plt.tight_layout()
        plt.show()


    def displayMFCCGraph(self, arr, int, x, y):
        S = librosa.feature.melspectrogram(arr, sr=int, n_mels=128)
        log_S = librosa.power_to_db(S, ref=np.max)
        mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=13)

        plt.figure(figsize=(12,4), num="MFCC Graph")
        librosa.display.specshow(mfcc)
        plt.ylabel('MFCC')
        plt.colorbar()
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(x+self.WINDOW_X_LOC, y + self.WINDOW_Y_LOC, self.GRAPH_WIDTH, self.GRAPH_HEIGHT)
        plt.tight_layout()
        plt.show()

    def getMetrics(self):
        pass


    def visualizeMetrics(self):
        pass

    def newCall(self):
        print("New")

    def openCall(self):
        print("Open")

    def exitCall(self):
        sys.exit(app.exec_())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


