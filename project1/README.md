# Project 1
This program bulk creates and moves files based on user input.
I created it because I have a large amount of files that I would like to be more organized based on the numeric sequence they are in.  These files are created by loading a video into a program called [VirtualDub2](https://sourceforge.net/projects/vdfiltermod/) and then doing an image sequence.  

  Included in the project1 folder are test files from a Kaltura video made for an English class. Example Output below is based on the example files video, not the actual project or the total Kaltura video due to file storage limitations listed below.  

  Due to github free account storage limitations, not all of the files in the test folder (storage limitation is 1GB, test file output is 1.33GB).  I have included the first 1000 files.  

  For comparison's sake, the actual project is a 39m26s video of 71,302 frames and the image file total size is between 20 and 40GB. 





To run this program, make sure Python3 is installed and working.

If using Windows, type:  
  ```python --version```

If using Linux, you may need to specify Python3:  
  ```python3 --version```


From the project1 folder that contains bulkfilemover.py, run the program using Python  
  ```python bulkfilemover.py```

Example Test Output:
```
$python bulkfilemover.py
How many files do you have?
1000
How many folders would you like?
10
How many files per folder would you like?
100
Where is the parent directory located?
C:\project1
What would you like the folders called? example-
Folder example-1 created
Folder example-2 created
...
Folder example-10 created

What is the filename prefix? example
What is the file extension? .jpeg
example-(00001-00100).jpeg moved into example-1
example-(00101-00200).jpeg moved into example-2
...
example-(00901-01000).jpeg moved into example-10
```