# PyDj

This project was meant to help understand GUI development with PyQT5 (Note this is raw, not utilizing Qt Designer), and make a simple application that can read, write, analyze, and visualize audio files in any format. The final display will allow users to see graphs covering frequency, pitch, tempo, and MFCC throughout the entire file or song. The purpose of this was to not only practice graphing and using data visualization libraries, but to help DJs determing the best location to mix a song with another. The metrics included help uncover the location that best marks an opening for the transition to another song. Pitch and BPM are important for this. I also wanted to play around with web scraping using Beautiful Soup to scrape images off of instagram. When the user types in the 'Artist' textbox, the input is sent as a request to instagram's hashtag page. This was the easiest idea I had in mind to get an image of the artist, however it is not anywhere near always accurate. Because the hashtag has no filtration system to determine if it is actually related to the artist, we will end up with some random pictures (sometimes pretty funny). 

## Future Features/Fixes
   * Embed the graphs in the display so that when you click they do not go off screen -- could perhaps be fixed by saving graphs as images and importing those rather than the graph itself
   * Export to CSV - Focus on graph features/specifics and possibly information on the artist
   * Transition scraping to **Genius Annotations** So that the information is much more accurate, and the images actually reflect the artist
   * Some way to read the audio and determine the song through that, something like Shazam (however hopefully there is a library or api out there!)
   * Make everything responsive, not absolute positioning
   * Attempt the recreate in *QtDesigner* and compare difficulty/efficiency/freedom

## Built With
   * [PyQt5](https://pypi.org/project/PyQt5/) - GUI Framework used
   * [Matplotlib](https://matplotlib.org/3.1.0/contents.html) - Graphing/Data visualization
   * [Librosa](https://librosa.github.io/librosa/) - Data analysis/visualization
   * [urllib](https://docs.python.org/3/library/urllib.html)
   * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - scraping images off instagram
   * [Playsound](https://pypi.org/project/playsound/) - playing audio input

## Screen Captures
   ![Capture 1](https://github.com/BrandontMitchell/PyDj/blob/master/PyDj/Assets/pydj_final.PNG?raw=true)

## Acknowledgements
* Icons made by [Flaticon](https://www.flaticon.com/authors/smashicons)

