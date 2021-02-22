# Project 1

This program bulk creates folders and moves files based on user input.
I wrote it because I have a large amount of files that I would like to be more organized based on the numeric sequence they are in.  These files are created by loading a video into a program called [VirtualDub2](https://sourceforge.net/projects/vdfiltermod/) and then doing an image sequence.

  Included in the project1 folder are test files from a Kaltura video made for an English class. Example Output below is based on the first 1000 frames from the test video, not the actual project or the total Kaltura video due to file storage limitations listed below. 

  Due to github free account storage limitations, not all of the files in the `testfiles` folder (storage limitation is 1GB, test file output is 1.33GB).  I have included the first 1000 files (73MB).  
  For comparison's sake, the actual project is a 39m26s video of 71,302 frames and the image file total size is 38.5GB.

To run this program, make sure Python3 is installed and working.
If using Windows, type:  
  ```python --version```
If using Linux, you may need to specify Python3:  
  ```python3 --version```


Usage instructions
1. copy the files located in `example files` to a directory of your choosing
2. From the project1 folder that contains bulkfilemover.py, run the program using Python  
```python bulkfilemover.py```
3. Follow the instructions on screen.

Example Test Output:
```
$python bulkfilemover.py
How many folders would you like?
10
Where is the parent directory located? Include trailing / or \
C:\project1\
What would you like the folders called? example-
Folder example-01 created
Folder example-02 created
...
Folder example-10 created

What is the last filename number? 1000
example-(00001-00100).jpeg moved into example-01
example-(00101-00200).jpeg moved into example-02
...
example-(00901-01000).jpeg moved into example-10
```

## Known issues
1. Amount of files per directory is hardcoded to 100.
2. Linux (and possibly Mac): example-00999.jpeg and example-01000.jpeg do not move over. This behavior does not happen on Windows.
3. Really only works with the example files and not the actual project files that I have.