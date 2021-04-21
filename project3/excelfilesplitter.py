import pandas
#Pandas has a built in read_excel function
# https://pandas.pydata.org/docs/user_guide/io.html
import numpy
#used to split the arrays of data into the split files.
import openpyxl
# Python library to help read/write excel files
# https://openpyxl.readthedocs.io/en/stable/

# initialize a counter for a for loop later
i = 0
print("How many rows would you like to split it into?")
rowsize = input()

while rowsize.isdigit() == False:
    # checking that the rowsize is a number.
    print("That is not a number. Please enter a number:")
    rowsize = input()

print("Please enter a filename with extension that ends in csv or xlsx")
userFile = input()

while not(userFile.endswith(('.xlsx', '.csv'))):
    #Checking the user input to make sure we have a valid file.
    print("That is not a valid file extension. Please enter a filename with extension that ends in csv or xlsx")
    userFile = input()

if userFile.endswith('.xlsx'):
    #xlsx loop to split the file
    dataFile = pandas.read_excel(userFile, index_col=0, engine="openpyxl")
    for row in numpy.array_split(dataFile, len(dataFile) // int(rowsize)):
        row.to_excel("split_{:02d}.xlsx".format(i), index=True)
        i += 1
elif userFile.endswith('.csv'):
    #csv loop
    dataFile = pandas.read_csv(userFile, index_col=0)
    for row in numpy.array_split(dataFile, len(dataFile) // int(rowsize)):
        row.to_csv("split_{:02d}.csv".format(i), index=True)
        i += 1