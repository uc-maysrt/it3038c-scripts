import os
#I have only tested this on Windows since that is how I create the source files of the project.
#In theory, the os.* commands should be plaform agnostic and it will work on Linux/Mac

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
#creates folders
# runs through a while loop until there are no new folders to create.
while 0 < numFolders:
    folderName = folderPrefix + str(numFolders)
    #Not really reused from another source but:
    # https://docs.python.org/3/library/os.html for finding the os.commands
    # https://www.geeksforgeeks.org/python-os-mkdir-method/ for more clarification, also the parentDir idea
    newPath = os.path.join(parentDir,folderName)
    os.mkdir(newPath)
    print("Folder " + folderName + " created")
    #counts down the number. https://datatofish.com/while-loop-python/
    # sort of for the source because I had forgotten to count down originally...
    numFolders = numFolders - 1
#moves files into previously created folders based on filenames/user input
print("What is the filename prefix?")
filenamePrefix = input()
print("What is the filename extension?")
fileExtension = input()
#runs through a while loop until there are no more files to move.
while 0 < numFiles:
    os.(something/to/make/the/files/move/to/dir)
    print("File " + filevariableundefinedatthemoment + " has been moved to " + folderNameGoesHere)
    numFiles = numFiles - 1
#os.sys("")