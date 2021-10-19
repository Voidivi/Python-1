# Assignment Week 4 - Dice Roll Simulator Program
# Author: Lyssette Williams
#!/usr/bin/env python3
import random

#I made the min and max values global since global variables were part of the chapter

min_value = 1
max_value = 6

#Function 1: stores the code that gets input from the user and then calls other functions

def main():
  display_title()
  userInput = input('Roll the dice? (y/n):')
  while userInput == 'y' or userInput == 'Y':
    roll_dice()
    userInput = input('Roll again? (y/n):')
  print('Thanks for playing!')

#Function 2: stores the program title
#Note: Assignment says title of program is 'Dice Roller' but on the homework sample program the title was displayed as 'Welcome to Dice Roller!'
#I chose the welcome message because it seemed appropriate for a game

def display_title():
  print('Welcome to Dice Roller!')
  print('')

#Function 3: simulates rolling a single die and returns the value

def roll():
  result = random.randint(min_value,max_value)
  return result 
  
#Function 4: rolls and stores the value of 2 die and will calculate
#The homework sample program's formatting was inconsistent (snake eyes was spaced out but boxcars was not) so I opted to just leave it un-spaced out

def roll_dice():
  roll_1 = roll()
  roll_2 = roll()
  total = roll_1 + roll_2
  print('Die 1:', roll_1)
  print('Die 2:', roll_2)
  print('Total', int(total))
  if total == 2:
    print('Snake Eyes!')
  elif total == 12:
    print('Boxcars!')
  print('')

  
if __name__ == "__main__":
	main()