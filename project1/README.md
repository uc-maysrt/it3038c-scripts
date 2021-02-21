# Project 1
This program bulk creates and moves files based on user input.  I created it because I have a large amount of files that I would like to be more organized based on the numeric sequence they are in.
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
70000
How many folders would you like?
70
How many files per folder would you like?
1000
Where is the parent directory located?
C:\project1
What would you like the folders called? folder-
Folder folder-1000 created
Folder folder-2000 created
...
Folder folder-70000 created

What is the filename prefix? filename
What is the file extension? .jpg
filename(1-1000).jpg moved into folder1000
filename(1001-2000).jpg moved into folder2000
...
filename(69001-70000).jpg moved into folder70000
```