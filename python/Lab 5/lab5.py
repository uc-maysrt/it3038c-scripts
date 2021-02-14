import time, random
from datetime import datetime, timedelta, date
#Take a birthday input and calculate how many seconds old you are
print("Please enter your birthday")
birthYear=int(input("Year:"))
birthMonth=int(input("Month (1-12):"))
birthDay=int(input("Day:"))
birthDate = datetime(birthYear, birthMonth, birthDay)
todaysDate = datetime.today()
newDate = todaysDate - birthDate
newDateseconds = int(newDate.total_seconds())
print("Your age in seconds is " + str(newDateseconds))

#5 second sleep before the next one
time.sleep(5)
#Take a word as input and count how many letters, how many vowels, and how many consonants
#Taken from stackoverflow
# https://stackoverflow.com/a/25885108
def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+1
    return num_vowels
def countconsonants(string):
    num_consonants=0
    for char in string:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            num_consonants = num_consonants+1
    return num_consonants
print("Please enter a word:")
yourWord = input()
while(True):
    if yourWord.isalpha() == True:
        print("The amount of letters in " + yourWord + " is " + str(len(yourWord)) + ". The amount of vowels is " + str(countvowels(yourWord)) + ". The amount of consonants is " + str(countconsonants(yourWord)) )
#breaks so it doesn't get stuck in a loop.
        break
    elif yourWord.isalpha() == False:
#repeats until a word is given.
        yourWord = input("That is not a word.  Please enter a word:")

#5 second sleep before the next one
time.sleep(5)

#Take a number input and calculate how many prime numbers come between it and 0
#print("Please enter a number:")
#primeNum = int(input())
#print("")

#5 second sleep before the next one
time.sleep(5)

#Write a 'guess the number game' where a random number is generated and the user must guess the number.
##The program says if their number is too high or too low until the right answer is guessed.
correctNumber = random.randint(0,100)
print("Please enter a number between 0 and 100:")
myGuess = input()
while True:
    if myGuess.isdigit() == False:
        print("That is not a number. Please enter a number:")
        myGuess =input()
    elif int(myGuess) < 0 or int(myGuess) > 100:
        print("That is not between 0 and 100. Please enter a number between 0 and 100:")
        myGuess = input()
    elif int(myGuess) != correctNumber:
        if int(myGuess) < correctNumber:
            print("Your guess is too low. Please enter a new guess:")
            myGuess = input()
        elif int(myGuess) > correctNumber:
            print("Your guess is too high. Please enter a new guess:")
            myGuess = input()
    else:
        print("Congratulations. You are correct.")
        break