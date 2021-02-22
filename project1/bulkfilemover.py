import os
import shutil
#I have only tested this on Windows since that is how I create the source files of the project.
#In theory, the os.* commands should be plaform agnostic and it will work on Linux/Mac

#gets some user input for later
print("How many files do you have?")
numFiles = int(input())
print("How many folders would you like?")
numFolders = int(input())
print("How many files per folder would you like?")
numFilesFolder = input()
print("Where is the parent directory located?")
parentDir = input()
print("What would you like the folders called?")
folderPrefix = input()
#throws the file listing into a list to call later.
fileList = os.listdir (parentDir)
#creates folders
# runs through a while loop until there are no new folders to create.
directoryList = []
while 0 < numFolders:
    folderName = folderPrefix + str(numFolders)
    #Not really reused from another source but:
    # https://docs.python.org/3/library/os.html for finding the os.commands
    # https://www.geeksforgeeks.org/python-os-mkdir-method/ for more clarification, also the parentDir idea
    newPath = os.path.join(parentDir,folderName)
    os.mkdir(newPath)
    print("Folder " + folderName + " created")
    #Throwing the directory into a list for later recall
    directoryList.append(newPath)
    #counts down the number. https://datatofish.com/while-loop-python/
    # sort of for the source because I had forgotten to count down originally...
    numFolders = numFolders - 1

#moves files into previously created folders based on filenames/user input
# None of these were necessary
# print("What is the filename prefix?")
# filenamePrefix = input()
# print("What is the filename extension?")
# fileExtension = input()
# print("What is the first filename number?")
# startFileNum = input()
# print("How many leading zeroes? Ex: 0000")
# leadingZeroes = input()

# this one is necessary for the while loop.
print("What is the last filename number?")
lastFileNum = input()

# initializing the variable for later.
fileCount = 0
#runs through a while loop until there are no more files to move.
#Discovered the main command through: https://docs.python.org/3/library/shutil.html
 
while 0 < numFiles and fileCount != lastFileNum:
#double conditional while loop.  Runs if the number of files is > 0 and as long as <variable> != lastFileNum
    if fileCount < 100:
        shutil.move(fileList[fileCount],newPath[0])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[0])
    elif 100 < fileCount < 199:
        shutil.move(fileList[fileCount],newPath[1])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[1])
    elif 200 < fileCount < 299:
        shutil.move(fileList[fileCount],newPath[2])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[2])
    elif 300 < fileCount < 399:
        shutil.move(fileList[fileCount],newPath[3])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[3])
    elif 400 < fileCount < 499:
        shutil.move(fileList[fileCount],newPath[4])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[4])
    elif 500 < fileCount < 599:
        shutil.move(fileList[fileCount],newPath[5])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[5])
    elif 600 < fileCount < 699:
        shutil.move(fileList[fileCount],newPath[6])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[6])
    elif 700 < fileCount < 799:
        shutil.move(fileList[fileCount],newPath[7])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[7])
    elif 800 < fileCount < 899:
        shutil.move(fileList[fileCount],newPath[8])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[8])
    elif 900 < fileCount < 999:
        shutil.move(fileList[fileCount],newPath[9])
        print("File " + fileList[fileCount] + " has been moved to " + newPath[9])
    #counts the number of files down by one
    numFiles = numFiles - 1
    #counts files moved up by one
    fileCount = fileCount + 1
#
#folderDeterminer = numFiles / numFilesFolder = numFolder