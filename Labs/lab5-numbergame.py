#Write a 'guess the number game' where a random number is generated and the user must guess the number.
##The program says if their number is too high or too low until the right answer is guessed.
import random

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