import requests
#I hate writer's block
print("What site would you like to search?")
myTarget = input()

print("Would you like to search through the cache? Yes or No")
searchCache = input()
while True:
    if searchCache !="Yes" or searchCache !="No":
        print("Please enter exactly Yes or No")
        searchCache = input()
    else:
        continue
print("Would you like to search for file extensions? Yes or No")
extQuestion = input()
while True:
    if extQuestion !="Yes" or extQuestion !="No":
        print("Please enter exactly Yes or No")
        extQuestion = input()
    elif extQuestion == "Yes":
        print("What file extension(s)? Separate by | Example: xls|doc")
        fileExt = input()
    else:
        continue

    if searchCache == "No" and extQuestion == "Yes":
        targetQuery = "site:" + myTarget + " ext:" + fileExt
    if searchCache == "No" and extQuestion == "No":
        targetQuery = "site:" + myTarget
    if searchCache == "Yes" and extQuestion == "No":
        targetQuery = "cache:" + myTarget
    else:
        print("You cannot use both cache and file extension at the same time")

targetSearch = requests.get(targetQuery)