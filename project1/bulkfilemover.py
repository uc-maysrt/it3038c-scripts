import os
#This version will work on Windows but not Linux/Mac [yet]
#os.system commands are as platform agnostic and
#technically run in Batch not powershell

#gets some user input for later
print("How many files do you have?")
numFiles = input()
print("How many folders would you like?")
numFolders = input()
print("How many files per folder would you like?")
numFilesFolder = input()

print("Where is the parent directory located?")
path = input()
print("What is the prefix?")
prefix = input()
print("What is the first filename?")
firstFile = input()
print("What is the last filename?")
lastFile = input()


#creates folders
os.system("mkdir")
print("")

#moves files into previously created folders based on filenames/user input
#os.sys("")