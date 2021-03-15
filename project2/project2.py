import requests
import os
userTarget = requests.get('http://www.uc.edu')
targetScrape = open("." + os.sep + "project2" + os.sep + "uc_homepage.html", 'w')
print(userTarget.text, file = targetScrape)
#This saves the webpage but the source has a lot of line breaks.
#Extension of the project is getting rid of the empty line breaks.
print("Web page is saved in uc_homepage.html")
targetScrape.close()
print("removing empty line breaks...")
targetScrape = open("." + os.sep + "project2" + os.sep + "uc_homepage.html", 'r')
cleanedFile = open("." + os.sep + "project2" + os.sep + "uc_homepage_cleaned.html", 'w')
line = targetScrape.readline()
for line in targetScrape:
    if line.rstrip():
        cleanedFile.write(line)
    #above adapted from: https://www.8bitavenue.com/remove-blank-lines-from-file-in-python/
targetScrape.close()
cleanedFile.close()
print("Done.")