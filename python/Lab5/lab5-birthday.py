from datetime import datetime, timedelta,date
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