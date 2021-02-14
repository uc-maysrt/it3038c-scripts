import random
#Write a 'guess the number game' where a random number is generated and the user must guess the number.
##The program says if their number is too high or too low until the right answer is guessed.

correctNumber = random.randint(0,9)
print("The correct number is " + str(correctNumber))
myGuess = 0
while myGuess != correctNumber:
    myGuess =input("Please enter a number:")
    if myGuess.isdigit():
        print("Yep. That's a number.")
        int(myGuess)
    else:
        myGuess =input("That is not a number. Please enter a number.")
        int(myGuess)
    if myGuess < correctNumber:
        print("Your guess is too low.")
        myGuess = int(input())
    elif myGuess > correctNumber:
        print("Your guess is too high.")
        myGuess = int(input())
    elif myGuess == correctNumber:
        print("Congratulations. You are correct.")