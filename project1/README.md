# Project 1
This program bulk creates and moves files based on user input.
I created it because I have a large amount of files that I would like to be more organized based on the numeric sequence they are in.  These files are created by loading a video into a program called [VirtualDub2](https://sourceforge.net/projects/vdfiltermod/) and then doing an image sequence.
Included in the project1 folder are test files from a Kaltura video made for an English class. Example Output below is based on the Kaltura video, not the actual project. Due to github free account storage limitations, not all of the files in the test folder (storage limitation is 1GB, test file output is 1.33GB)


To run this program, make sure Python3 is installed and working.

If using Windows, type:  
  ```python --version```

If using Linux, you may need to specify Python3:  
  ```python3 --version```


From the project1 folder that contains bulkfilemover.py, run the program using Python  
  ```python bulkfilemover.py```

Example Output:
```
$python bulkfilemover.py
How many files do you have?
10584
How many folders would you like?
11
How many files per folder would you like?
1000
Where is the parent directory located?
C:\project1
What would you like the folders called? folder-
Folder folder-1 created
Folder folder-2 created
...
Folder folder-11 created

What is the filename prefix? filename
What is the file extension? .jpg
filename(1-1000).jpg moved into folder-1
filename(1001-2000).jpg moved into folder-2
...
filename(10001-10584).jpg moved into folder-11
```