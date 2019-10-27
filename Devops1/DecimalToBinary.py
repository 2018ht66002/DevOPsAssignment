'''
PYTHON 3
Author: Sandeep Pillai (www.github.com/Corruption13)
Program: Decimal to Binary converter.
THis program accepts fractional values, the accuracy can be set below:
'''
decimal_accuracy = 7


def dtbconverter(num):  # Function inputs a float value and returns a list as output
    # Reasoning for list instead of integer: to avoid integer overflow error.

    whole = []  # The part before decimal point
    fractional = ['.']  # The part after decimal point

    decimal = round(num % 1, decimal_accuracy)  # Extract fractional number part of decimal
    w_num = int(num)  # Extract whole number part of decimal.

    i = 0  # Some fractional decimal numbers have infinite binary values, so we limit this loop below.

    # Loop to find binary of decimal part
    while (decimal != 1 and i < decimal_accuracy):
        decimal = decimal * 2
        fractional.append(int(decimal // 1))
        decimal = round(decimal % 1, decimal_accuracy)
        if (decimal == 0): break  # Removes trailing zeros.
        i = i + 1

        # Loop to find binary of whole number part.
    while (w_num != 0):
        whole.append(w_num % 2)
        w_num = w_num // 2
    whole.reverse()

    return whole + fractional  ### End of dtbconverter() - 16 lines


# Python program to Find day of 
# the week for a given date 
import calendar  #module of python to provide useful fucntions related to calendar
import datetime # module of python to get the date and time 


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() #this statement returns an integer corresponding to the day of the week
    return (calendar.day_name[born]) #this statement returns the corresponding day name to the integer generated in the previous statement


# Driver program 
date = '03 02 2019' #this is the input date
print(findDay(date))  # here we print the final output after calling the fucntion findday