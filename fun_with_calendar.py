# Calender Arithmetic


from datetime import datetime as dt

# current time
print(dt.now()) # this is system time
# 2024-10-08 10:04:29.814682 (814682 is milliseconds)

# if i want to know the time of some other location, they follow different timezone
# standard time is calculated as Greenwich Mean Time and indian time is ahead by 5 hours and 30 minutes(GMT+05:30)

import pytz
tz = pytz.timezone('Singapore')
print(dt.now(tz)) # 2024-10-08 12:39:14.676180+08:00 (means GMT+08:00)

# tz means timezone
# what if i don't know the timezone i.e somewhere it is same as country name
# somewhere it is different like timezone for India is Asia/Kolkata

# print(pytz.all_timezones) # we will get a list of all timezones
# print(len(pytz.all_timezones)) # 596


# if a friend ask on which day he was born if he tells the DOB then it's difficult to find.

import calendar

'''
In Python, calendar.weekday(year, month, day) returns an integer representing the day of the week for a given date. The result follows this convention:

0: Monday
1: Tuesday
2: Wednesday
3: Thursday
4: Friday
5: Saturday
6: Sunday
# Get the weekday for October 8, 2024
weekday = calendar.weekday(2024, 10, 8)
print(weekday)  # Output: 1, which means Tuesday
'''
print(calendar.weekday(2024,7,1)) # 0 means Monday

# Task 1
# Given a date, can you tell what day of the week it falls on
# Moths till July, odd numbered months have 31 while even numbered months has 30 days.
# And other months from Aug, odd numbered months have 30 while even numbered months has 31 days.

def check_leap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False

def check_valid_date(dt, m, y, l):
    if l:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==1:
                    if dt<31:
                        return True
                    else:
                        return False
                else:
                    if dt<32:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if dt<29:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==1:
                    if dt<31:
                        return True
                    else:
                        return False
                else:
                    if dt<32:
                        return True
                    else:
                        return False
'''
def check_valid_date(dt,m,y,l):
    if l:
        is_leap = True
    else:
        is_leap = False
    if 1 <= m <= 12:
        max_days = 29 if is_leap and m == 2 else calendar.monthrange(y, m)[1]
        return 1 <= dt <= max_days
    return False

The calendar.monthrange(y, m) function is used to determine the number of days in the month, which simplifies the entire process.

calendar.monthrange(year, month) returns two values:

The first value is the day of the week the month starts on (0 for Monday, 6 for Sunday).

The second value is the number of days in the month, which is what we are interested in.
'''

def get_day(d):
    list_of_days = ["Monday", "Tuesday", "Wednesday"," Thursday", "Friday", "Saturday", "Sunday"]
    return list_of_days[day_index]

while(1):
    year = int(input("Enter year(1970-2024):"))
    if year<1970:
        print("Enter a year starting from 1970")
    else:
        break

while(1):
    month = int(input("Enter month(1-12):"))
    if month<=12 and month>0:
        break
    else:
        print("Enter a valid month (1-12)")

leap = check_leap(year)
while(1):
    date = int(input("Enter date:"))
    if date>0 and check_valid_date(date, month, year, leap):
        break
    else:
        print("Enter a valid date")

day_index = calendar.weekday(year,month,date)
day = get_day(day_index)

print(date,"/",month,"/",year,"falls on",day)



# Task 2
# What is the current time as per different time zones?
'''
In Python, fabs() is a function from the math module that returns the absolute value of a floating-point number. Unlike the built-in abs() function, which works for all number types (integers and floats), math.fabs() is specifically designed to return the absolute value as a floating-point number, even if the input is an integer.

Key Points:
- fabs() always returns a float value.
- If you only need the absolute value and do not require a float, you can use Python's built-in abs() function, which works for all number types.
'''

from datetime import datetime as dt
import pytz

timezones = pytz.all_timezones

for i in range(len(timezones)):
    tz = pytz.timezone(timezones[i])
    print("Current time at zone",timezones[i],"is",dt.now(tz))
