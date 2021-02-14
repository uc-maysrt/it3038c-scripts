#Take a number input and calculate how many prime numbers come between it and 0
# for loop from:
#  https://www.javatpoint.com/pyhton-print-all-prime-number-in-an-interval
#Method #1:
#lower = int(0)
#print("Please enter a number:")
#myNum = input()
#for num in range(lower, int(myNum) + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
#Method #2:
def primeNum(myNum):
    lower = int(0)
    for num in range(lower, int(myNum) + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
print("Please enter a number:")
myNum = input()
while True:
    if myNum.isdigit() == False:
        print("That is not a number. Please enter a number:")
        myNum =input()
    else:
        primeNum(myNum)
        break