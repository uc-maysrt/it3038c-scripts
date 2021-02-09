import time
start_time = time.time()
print('What is your name?')
myName = input()
print("Hello, " + myName + ". That's a good name. How old are you?")
#Commenting out this to move on the %s part
#myAge = int(input())
#print(str(myAge)+"? That's funny, I am only a few seconds old.")
#print("I wish I was " + myAge * 2 + " years old")
#print("I wish I was " + str(myAge * 2) + " years old")
myAge = int(input())
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only a %s seconds old." % (myAge,programAge) )
print("I wish I was %s years old" % (myAge* 2))

time.sleep(3)
print("I'm tired. I sleep now.")