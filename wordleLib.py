# Authors: Cade Fandl, Ben Miller, Gabriel Sullivan
# This file main author: Gabriel Sullivan
# Majors: Computer Science, German Communication & Culture
# Creation date: November 14, 2025
# Due date: November 24, 2025
# Course: CPSC328-020
# Professor name: Mr. Walther
# Assignment: Group Assignment
# Filename: wordleLib.py
# Purpose: contains the library

import random

# Function name: getRandWord
# Purpose: selects a random word from a list and returns it
# Input: none
# Returns: string - the word selected
# Throws: none
def getRandWord():
    # Citation: referenced the following for lists:
    #           https://www.w3schools.com/python/python_lists.asp
    #           November 14, 2025
    words = ["APPLE", "BREAK", "ZEROS", "CRAPS", "GIVEN"]
    # Citation: referenced the following for random number generation:
    #           https://www.w3schools.com/python/module_random.asp
    #           https://www.w3schools.com/python/ref_random_randint.asp
    #           November 14, 2025
    randNum = random.randint(0, len(words) - 1) # generates a random int from 0 to the length of the list minus one
    return words[randNum]

# Function name: getGuessResults
# Purpose: takes in the guess and returns its correctness
# Input: string guess - the guess the user submitted
#        string 
# Returns: string - the word results with # meaning correct letter, correct spot
#                                         . meaning correct letter, wrong spot
#                                         - meaning letter not in correct word
# Throws: none
def getGuessResults(guess, correctWord):
    result = ""
    return result

# Citation: referenced for the below code:
#           https://stackoverflow.com/questions/8715990/python-how-to-tell-if-file-executed-as-import-vs-main-script
#           November 14, 2025
if __name__ == '__main__':
    print(getRandWord())
