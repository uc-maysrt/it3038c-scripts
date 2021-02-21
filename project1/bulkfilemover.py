import os
#This version will work on Windows but not Linux/Mac [yet]
#os.system commands are meant to be platform agnostic and
#technically runs in Batch not powershell

#gets some user input for later
print("How many files do you have?")
numFiles = input()
print("How many folders would you like?")
numFolders = int(input())
print("How many files per folder would you like?")
numFilesFolder = input()
print("Where is the parent directory located?")
parentDir = input()
print("What would you like the folders called?")
folderPrefix = input()
print("What is the filename prefix?")
filenamePrefix = input()
print("What is the filename extension?")
fileExtension = input()

#probably not needed?
#print("What is the first filename?")
#firstFile = input()
#print("What is the last filename?")
#lastFile = input()

#creates folders
# runs through a while loop until there are no new folders to create.
while 0 < numFolders:
    folderName = folderPrefix + str(numFolders)
    newPath = os.path.join(parentDir,folderName)
    os.mkdir(newPath)
    print("Folder " + folderName + " created")
    #counts down the number
    numFolders = numFolders - 1
#moves files into previously created folders based on filenames/user input
#os.sys("")