import pandas
# https://pandas.pydata.org/docs/user_guide/index.html
# Used for the Excel and CSV parts.
# https://pandas.pydata.org/docs/user_guide/io.html
import numpy
# https://numpy.org/doc/1.16/reference/routines.random.html
from faker.providers.person.en import Provider
import openpyxl

# https://www.caktusgroup.com/blog/2020/04/15/quick-guide-generating-fake-data-with-pandas/
# I didn't really change too much from this because the focus is more on the other python file.
def random_name(name_type, size):
    #Generates random names
    names=getattr(Provider, name_type)
    return numpy.random.choice(names, size=size)
def random_genders(size, p=None):
    #Generates genders
    if not p:
        p = (0.49, 0.49, 0.01, 0.01)
    gender = ("M", "F", "O", "")
    return numpy.random.choice(gender, size=size, p=p)
def random_dates(start, end, size):
    #Generates random dates
    divide_by = 24 * 60 * 60 * 10**9
    start_u = start.value // divide_by
    end_u = end.value // divide_by
    return pandas.to_datetime(numpy.random.randint(start_u, end_u, size), unit="D")
def random_active(size):
    active = ("Yes", "No")
    return numpy.random.choice(active, size=size)
print("How many rows would you like?")
size = int(input())
datafile = pandas.DataFrame(columns=['First', 'Last', 'Gender', 'Birthdate', 'Active'])
datafile['First'] = random_name('first_names', size)
datafile['Last'] = random_name('last_names', size)
datafile['Gender'] = random_genders(size)
datafile['Birthdate'] = random_dates(start=pandas.to_datetime('1940-01-01'), end=pandas.to_datetime('2000-01-01'), size=size)
datafile['Active'] = random_active(size)

# built in functionality of pandas
# https://pandas.pydata.org/docs/user_guide/io.html#io-store-in-csv
datafile.to_csv('this-file-is-fake-data.csv')
print("CSV file has been generated.")
# built in function of pandas but needs openpyxl for the engine, especially for the xls file.
# https://pandas.pydata.org/docs/user_guide/io.html#io-excel-writer
datafile.to_excel('this-file-is-fake-data.xlsx', engine="openpyxl")
print("Excel file has been generated.")
