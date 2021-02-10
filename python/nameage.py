import time
start_time = time.time()
print('What is your name?')
myName = input()

#while loop example
while myName != "Robert":
    if myName == 'your name':
        print("Not funny, Dad. What's your real name?")
        myName=input()
    else:
        print("That is not your name. Please tell me your name.")
        myName=input()
    #print("This is not your name. Please type 'your name'.")
    #myName = input()


print("Hello, " + myName + ". That's a good name. How old are you?")
#Commenting out this to move on the %s part
#myAge = int(input())
#print(str(myAge)+"? That's funny, I am only a few seconds old.")
#print("I wish I was " + myAge * 2 + " years old")
#print("I wish I was " + str(myAge * 2) + " years old")
myAge = int(input())

#Sample if statements
if myAge < 13:
    print("Learning young, that's good")
elif myAge == 13:
    print("You're a teenager now...that's cool, I guess.")
elif myAge < 13 and myAge < 30:
    print("Still young, still learning...")
elif myAge >= 30 and myAge < 65:
    print("Now you're adulting...")
else:
    print("...you've lived a long time?")
time.sleep(1)
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only a %s seconds old." % (myAge,programAge) )
print("I wish I was %s years old" % (myAge* 2))

time.sleep(3)
print("I'm tired. I sleep now.")