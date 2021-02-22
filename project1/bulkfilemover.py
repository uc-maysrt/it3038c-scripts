import os
import shutil
#I have only tested this on Windows since that is how I create the source files of the project.
#In theory, the os.* and shutil commands should be plaform agnostic and it will work on Linux/Mac

#gets some user input for later

# This is unnecessary because the numbers per folder are hardcoded for now
#print("How many files do you have?")
#numFiles = int(input())

print("How many folders would you like?")
numFolders = int(input())

# This is unnecessary because the number of files per folder are hardcoded for now
#print("How many files per folder would you like?")
#numFilesFolder = input()

#Since Windows does \ but Mac+Linux does /
#added the prompt about add the trailing slash
print("Where is the parent directory located? Include trailing / or \\")
parentDir = input()
print("What would you like the folders called?")
folderPrefix = input()

#throws the file listing into a list to call later.
# discovered at https://www.tutorialspoint.com/python/os_listdir.htm 
fileList = os.listdir( parentDir )
#initialize an empty list that will be added to during the while loop.
directoryList = []

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
lastFileNum = int(input())

# initializing the variable for later.
fileCount = 0
#runs through a while loop until there are no more files to move.
#Discovered the main command through: https://docs.python.org/3/library/shutil.html
 
while fileCount != lastFileNum:
#was a double conditional while loop. the first condition has been rendered unnecessary for the time being.
# first condition was "0 < numFiles" Runs if the number of files is > 0
# second/currently only condition runs as long as fileCount does not equal the last file number put in by the user
# should add error checking.

#Because of how the directoryList list was constructed, it iterates through the list backwards.
    if fileCount < 100:
        shutil.move(parentDir + fileList[fileCount],directoryList[9])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[9])
    elif 100 <= fileCount <= 199:
        shutil.move(parentDir + fileList[fileCount],directoryList[8])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[8])
    elif 200 <= fileCount <= 299:
        shutil.move(parentDir + fileList[fileCount],directoryList[7])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[7])
    elif 300 <= fileCount <= 399:
        shutil.move(parentDir + fileList[fileCount],directoryList[6])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[6])
    elif 400 <= fileCount <= 499:
        shutil.move(parentDir + fileList[fileCount],directoryList[5])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[5])
    elif 500 <= fileCount <= 599:
        shutil.move(parentDir + fileList[fileCount],directoryList[4])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[4])
    elif 600 <= fileCount <= 699:
        shutil.move(parentDir + fileList[fileCount],directoryList[3])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[3])
    elif 700 <= fileCount <= 799:
        shutil.move(parentDir + fileList[fileCount],directoryList[2])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[2])
    elif 800 <= fileCount <= 899:
        shutil.move(parentDir + fileList[fileCount],directoryList[1])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[1])
    elif 900 <= fileCount <= 999:
        shutil.move(parentDir + fileList[fileCount],directoryList[0])
        print("File " + fileList[fileCount] + " has been moved to " + directoryList[0])
#counts the number of files down by one ->rendered unnecessary
#    numFiles = numFiles - 1
    #counts files moved up by one
    fileCount = fileCount + 1