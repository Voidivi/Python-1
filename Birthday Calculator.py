#!/usr/bin/env python3
# Assignment Week 7 - Birthday Calculator
# Author: Lyssette Williams

from datetime import *

# main will get the user input, call on display, run the while statement and say goodbye
def main():
    display()
    cont_program = 'y'
    while cont_program == 'y' or cont_program == 'Y':
        userinput = input('Please enter your name: ')
        userbday = input('Please enter your birthdate (MM/DD/YYYY):')
        birthday(userinput, userbday)
        cont_program = input('Continue? (y/n): ')
        print('=' * 36)
    print('Bye!')

#display  is purely formatting, I guess I could cut down on space used by putting both print statements in main
def display ():
    print('Welcome to Birthday Calculator!')
    print('='*36)

# birthday will convert the user input date twice, it will also display today's date in the format requested
# it will call on calc_age and when_party to run
def birthday(userinput, userbday):   
    bday = datetime.strptime(userbday,'%m/%d/%Y')
    print('Birthday:', bday.strftime('%A, %B, %d, %Y')) 
    print('Today:', date.today().strftime('%A, %B, %d, %Y'))
    calc_age(userinput,bday)
    when_party(userinput, bday)

# when_party figures out when the user's birthday is (past,present,future)

def when_party(userinput, userbday):
    today = date.today() 
    is_birthday = date(today.year, userbday.month, userbday.day)
    if is_birthday < today:
        is_birthday = date(today.year+1, userbday.month, userbday.day)
    days_until = (is_birthday - today).days
    if today == is_birthday:
        print(userinput + '\'s birthday is today!')
    elif today == date(today.year, is_birthday.month, is_birthday.day+1):
        print (userinput + '\'s birthday was yesterday!')
    elif today == date(today.year, is_birthday.month, is_birthday.day-1):
        print(userinput + '\'s birthday is tomorrow!')
    else:
        print(userinput + '\'s birthday is in ' + str(days_until) + ' days')        

# calc_age figures out the user age, and converts to days if under 2 years old
# I just think it's weird to use days or months - why do we do that?
# Also calc_age went through a couple iterations and feels like an absolute busy mess but it works

def calc_age(userinput, userbday):
    today = date.today()
    todaysdate = datetime(today.year, today.month, today.day)
    timespan = todaysdate - userbday
    isdays = True # under 2 years old
    if timespan.days/365 > 2:
        isdays = False
    elif timespan.years/365 == 2:
        if userbday.month > today.month:
            isdays = True   # under 2 years old
        elif userbday.month < today.month:
            isdays = False
        else: 
            if userbday.day > today.day: 
                isdays = True # under 2 years old
            elif userbday.day <= today.day:
                isdays = False
    else: 
        isdays = True # under 2 yeasrs old
    if isdays:
        value = timespan.days
        units = 'days'
    else:
        value = int(timespan.days/365)
        units = 'years'
    print(userinput + ' is '+ str(value) + ' ' + units + ' old.')


if __name__ == "__main__":
  main() 

