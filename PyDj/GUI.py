from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QVBoxLayout, QPushButton, QAction, QSizePolicy, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import requests, random, librosa, librosa.display, time, os, sys, urllib, ssl, json
from matplotlib.figure import Figure 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs 
from playsound import playsound
import matplotlib.pyplot as plt 
import numpy as np


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

    SUMMARY_BG_X = SUMMARY_DESC_X+30
    SUMMARY_BG_Y = IMPORT_BTN_Y+75
    SUMMARY_BG_WIDTH = GRAPH_BG_WIDTH/2.6
    SUMMARY_BG_HEIGHT = GRAPH_BG_HEIGHT*1.4

    PLAY_BG_X = SUMMARY_DESC_X+25
    PLAY_BG_Y = IMPORT_BTN_Y+665
    PLAY_BG_WIDTH = 160
    PLAY_BG_HEIGHT = 95     
    artist = ''
    song = ''

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
        self.graphBackground(self.SUMMARY_DESC_X-15, self.SUMMARY_BG_Y, self.SUMMARY_BG_WIDTH, self.SUMMARY_BG_HEIGHT, 'summarybg.jpg')
        self.graphBackground(self.PLAY_BG_X, self.PLAY_BG_Y, self.PLAY_BG_WIDTH, self.PLAY_BG_HEIGHT, 'summarybg.jpg')

        self.createSummary(self.SUMMARY_BG_X, self.SUMMARY_BG_Y, "---  BREAKDOWN  ---")
        self.createBPM(self.SUMMARY_DESC_X, self.SUMMARY_BG_Y+75, "BPM: ")
        self.createFREQ(self.SUMMARY_DESC_X, self.SUMMARY_BG_Y+125, "Max Freq: ")
        self.trackSpecs(self.SUMMARY_DESC_X, self.SUMMARY_BG_Y+175)
        

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
        self.summaryLabel = QLabel(text,self)
        self.summaryLabel.resize(1000, 20)
        self.summaryLabel.move(x, y)

    def createBPM(self, x, y, text):
        self.bpmLabel = QLabel(text, self)
        self.bpmLabel.resize(1000,20)
        self.bpmLabel.move(x, y)

    def createFREQ(self, x, y, text):
        self.freqLabel = QLabel(text, self)
        self.freqLabel.resize(1000, 20)
        self.freqLabel.move(x, y)
    
    def trackSpecs(self, x, y):
        self.trackLabel = QLabel("Track Name: ", self)
        self.artistLabel = QLabel("Artist: ", self)
        self.genreLabel = QLabel("Genre: ", self)
        
        self.trackLabel.resize(1000, 20)
        self.trackLabel.move(x, y)
        self.artistLabel.resize(1000, 20)
        self.artistLabel.move(x, y+50)
        self.genreLabel.resize(1000, 20)
        self.genreLabel.move(x, y+100)
        

    def suggestSongs(self, x, y, text):
        self.newSongs = QLabel(text, self)
        self.newSongs.move(x, y)

    def openFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        try:
            self.getAudioMetrics(name[0])
            self.playButton(self.SUMMARY_DESC_X+30, self.IMPORT_BTN_Y+670, 150, 85, name[0])
        except:
            print("No Audio Selected")

    def playFile(self, file):
        playsound(file)

    def graphBackground(self, x, y, width, height, image):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(os.path.join("Assets", image)))
        self.label.setGeometry(x, y, width, height)

    def getInfo(self, hashtag, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = bs(html, 'html.parser')
        script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
        
        page_json = script.text.split(' = ', 1)[1].rstrip(';')
        data = json.loads(page_json)
        for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
            image_src = post['node']['thumbnail_resources'][1]['src']
            hs = open(os.path.join("Assets\ArtistTextFiles", hashtag + '.txt'), 'a')
            hs.write(image_src + '\n')
            hs.close()

        with open(os.path.join("Assets\ArtistTextFiles", hashtag + '.txt')) as f:
            self.content = f.readlines()

        image = self.content[random.randint(0, len(self.content)-1)]
        filename = os.path.join("Assets\ArtistsImages", hashtag+".jpg")
        urllib.request.urlretrieve((image), filename)
        self.importPicture(20, 610, 240, 240, filename)

    def importPicture(self, x, y, width, height, image):
        self.artistPic = QLabel(self)
        self.artistPic.setPixmap(QPixmap(image))
        self.artistPic.setGeometry(x, y, width, height)
        self.artistPic.show()

    def playButton(self, x, y, width, height, filename):
        self.playbtn = QPushButton(self)
        self.playIcon = QIcon(os.path.join("Assets", "playbtn_blank.png"))
        self.playbtn.setIcon(self.playIcon)
        self.playbtn.setGeometry(x, y, width, height)
        self.playbtn.show()
        time.sleep(3)
        self.playbtn.clicked.connect(lambda: self.playFile(filename))

##################      ANALYSIS     ##################
    
    def getTitle(self):
        self.artist = self.artistLine.text()
        self.song = self.songLine.text()
        self.artistLabel.setText("Artist: " + self.artist)
        self.trackLabel.setText("Track Name: " + self.song)

        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False 
        self.ctx.verify_mode = ssl.CERT_NONE

        url = 'https://www.instagram.com/explore/tags/' + self.artist.replace(" ", "") #hashtags have no spaces
        self.getInfo(self.artist.replace(" ", ""), url)


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

        # loops through genre dictionary to match bpm from input file
        # to a specific genre, helpful when mixing
        for key, value in genreDict.items():
            if int(tempo) in value:
                genre = key

        self.bpmLabel.setText("BPM: " + str(int(tempo)))
        self.genreLabel.setText("Genre: " + genre)
        self.displayFreqGraph(y, sr, self.FREQ_GRAPH_X, self.FREQ_GRAPH_Y)
        self.displayPitchGraph(y, sr, self.PITCH_GRAPH_X, self.PITCH_GRAPH_Y)
        self.displayBeatGraph(y, sr, self.BEAT_GRAPH_X, self.BEAT_GRAPH_Y)
        self.displayMFCCGraph(y, sr, self.MFCC_GRAPH_X, self.MFCC_GRAPH_Y)        

    def displayFreqGraph(self, arr, samplerate, x, y):
        librosa.display.waveplot(arr, sr=samplerate)
        plt.title("Freq Detection")
        self.maxFreq = arr.max()
        self.freqLabel.setText("Max Freq: " + str(self.maxFreq))
        
        # Only way to resize figure
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
        
        # Only way to resize figure
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

        # Only way to resize figure
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

        # Only way to resize figure
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(x+self.WINDOW_X_LOC, y + self.WINDOW_Y_LOC, self.GRAPH_WIDTH, self.GRAPH_HEIGHT)
        plt.tight_layout()
        plt.show()


    # Handles file i/o and exiting application
    def newCall(self):
        self.artistLabel.setText("Artist: ")
        self.trackLabel.setText("Track Name: ")
        self.bpmLabel.setText("BPM: ")
        self.genreLabel.setText("Genre: ")
        self.artistPic.hide()

    def openCall(self):
        self.openFile()

    def exitCall(self):
        sys.exit(app.exec_())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())