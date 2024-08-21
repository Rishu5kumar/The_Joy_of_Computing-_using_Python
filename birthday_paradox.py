# here we will generate birth date randomly
# birth date will be generated according to birth month
# we are not concerned about birth year

# most of the years that can be divided by 4 are leap years
# exception: century years are not leap years unless they are divided by 400, ex:- 1700 is not a leap year

# if year divisible by 400 is leap_year
# else if year is divisible by 100 then not_leap_year
# else if year is divisible by 4 then is_leap_year
# else not_leap_year


# sudo code for birth date

'''
if month is February and year is leap year then
Generate day randomly from 1 to 29
if month is February and year is not a leap year then
Generate day randomly from 1 to 28
if month%2==0 and month<7 then // April and June
Generate day randomly from 1 to 30
if month%2==0 and month>7 then // august, October and December
Generate day randomly from 1 to 31
if month%2!=0 and month<=7 then // January, March, May, July
Generate day randomly from 1 to 31
if month%2!=0 and month>7 then // September and November
Generate day randomly from 1 to 30
'''

from collections import Counter
import random
import datetime
birthday = []
i=0
while i<50:
    year = random.randint(1902,2024) # as oldest person ever lived was 122 yr old
    print("Year is: ",year)
    if(year%400==0 or (year%100!=0 and year%4==0)):
        leap = 1
    else:
        leap = 0
    month = random.randint(1,12)
    print("Month chosen is: ", month)
    if(month == 2 and leap == 1):
        day = random.randint(1,29)
        print("Day is from 1st condition: ",day)
    elif(month == 2 and leap == 0):
        day = random.randint(1,28)
        print("Day is from 2nd condition: ",day)
    elif(month==7 or month==8):
        day = random.randint(1,31)
        print("Day is from 3rd condition: ",day)
    elif(month%2 == 0 and month>7 and month<12):
        day = random.randint(1,31)
        print("Day is from 4th condition: ",day)
    elif(month%2!=0 and month<7):
        day = random.randint(1,31)
        print("Day is from 5th condition: ",day)
    else:
        day = random.randint(1,30)
        print("Day is from 6th condition: ",day)

    dd = datetime.date(year, month, day) # we can follow any other method like day, month, year
    print("Whole date is: ", dd)
    day_of_year = dd.timetuple().tm_yday # it will give day of year directly
    print("Day of year is: ",day_of_year)
    birthday.append(day_of_year)
    print("Iteration ",i+1," has been over")
    i+=1

birthday.sort()
i=0
while i<50:
    print(birthday[i])
    i+=1

def find_duplicates(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count > 1]

duplicates = find_duplicates(birthday)
print("Collided Days of year are: ", duplicates)

# Exploring datetime library
print(datetime.date.today()) # 2024-08-21
print(datetime.date.today().strftime("%Y")) # 2024
print(datetime.date.today().strftime("%B")) # for month, August
print(datetime.date.today().strftime("%d")) # 21 (they are string)

# displaying week number of the year
print(datetime.date.today().strftime("%W")) # 34

# displaying weekday of the week
print(datetime.date.today().strftime("%w")) # 3 

# displaying the day of the year
print(datetime.date.today().strftime("%j")) # 234

# displaying the day of the week
print(datetime.date.today().strftime("%A")) # Wednesday

# displaying the current time
print(datetime.datetime.now()) # 2024-08-21 13:44:24.271631
