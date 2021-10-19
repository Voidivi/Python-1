#!/usr/bin/env python3
# Assignment Week 6 - Pig Latin Translator
# Author: Lyssette Williams

# global values for the program
ay = 'ay'
way = 'way'
vowels = ['a','e', 'i', 'o', 'u']
punctuations = '''!()-[];:'",<>./?@#$%^&*_~'''

# decided to add some formatting stuff to make it more readable
def display():
  print('Welcome to the Pig Latin Translator!')
  print('=' * 36)

# I struggled for many hours on how to get this program working for more than one word
# I got it working great for one word only
# I also tried the strip function (after you talked about it in zoom) 
# but since it wouldn't pull punctuation out from the middle of a sentence I went back to for loop

def piglatin():
  userinput = input('Enter text: ')
  no_punct = ""			
  for char in userinput:			#stripping punctionation
    if char not in punctuations:
      no_punct = no_punct + char
  no_punct = no_punct.lower()
  userinput = no_punct 		  #converting the no punctuation variable back to userinput so I can do less renaming work downstream
  print('English:', userinput)
  userinput = userinput.split()  #splitting out words
  translation = ''
  for word in userinput: #searching for vowels
    first = word[0]
    if first in vowels:
      translation = translation + word + way + ' '
    else:
      for char in word[1:]:
        if char in vowels or char == 'y':    #dealing with y
          translation = translation + word[word.index(char):] + word[0:word.index(char)] + ay + ' '  
          break
  print('Pig Latin:', translation)
  
# again added some formatting for legibility
def main():
  display()
  cont_program = 'y'
  while cont_program == 'y' or cont_program == 'Y':
    piglatin()
    cont_program = input('Continue? (y/n): ')
    print('=' * 36)
  print('Bye!')

if __name__ == "__main__":
  main() 

