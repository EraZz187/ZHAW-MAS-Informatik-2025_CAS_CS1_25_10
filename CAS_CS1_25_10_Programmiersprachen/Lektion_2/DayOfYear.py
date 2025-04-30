' A leap year is divisible by 4, but not divisible by 100, unless its divisible by 400'
from numba.np.npdatetime import is_leap_year

date = input("please enter a date: ") #dd.mm.yyyy

day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

is_leap_year = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

if is_leap_year:
    daysInMonth[1] = 29

for i in daysInMonth:
    days += daysInMonth[i]
