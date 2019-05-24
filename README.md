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
   *



Icon reference: <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>