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