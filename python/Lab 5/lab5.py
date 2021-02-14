import time, random

#Take a birthday input and calculate how many seconds old you are

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
if yourWord.isalpha():
    print("The amount of letters in" + yourWord + " is " + str(len(yourWord)) + ". The amount of vowels is " + str(countvowels(yourWord)) + ". The amount of vowels is " + str(countconsonants(yourWord)) )
else:
    yourWord = input("That is not a word.  Please enter a word:")

#Take a number input and calculate how many prime numbers come between it and 0
#print("Please enter a number:")
#primeNum = int(input())
#print("")

#Write a 'guess the number game' where a random number is generated and the user must guess the number.
##The program says if their number is too high or too low until the right answer is guessed.
#correctNumber = random.randint(0,9)
#print("The correct number is " + str(correctNumber))
#myGuess = 0
#while myGuess != correctNumber:
#    myGuess =input("Please enter a number:")
#    if myGuess.isdigit():
#        print("Yep. That's a number.")
#        int(myGuess)
#    else:
#        myGuess =input("That is not a number. Please enter a number.")
#        int(myGuess)
#    if myGuess < correctNumber:
#        print("Your guess is too low.")
#        myGuess = int(input())
#    elif myGuess > correctNumber:
#        print("Your guess is too high.")
#        myGuess = int(input())
#    elif myGuess == correctNumber:
#        print("Congratulations. You are correct.")