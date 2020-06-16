#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def calculate(string):
    p = 131
    M = pow(10,9) + 7
    total = 0
    letters = list(string)

    length = len(letters) - 1
    for letter in letters:
        if length == 0:
            total += ord(letter) % M
        else:
            total += ord(letter)*pow(p,length)
        length -= 1

    return total

def populatePassword(letters):
    numbersAndLetters = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    bag = []
    for i in numbersAndLetters:
        bag.append(calculate(letters+i))

    return bag


def authEvents(events):
    # Write your code here
    numbers = ["1","2","3","4","5","6","7","8","9"]
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    realHash = 0
    populatedPassword = []
    result = []
    for event in events:
        print(events)
        if event == 'setPassword':
            password = event[1]
            realHash = calculate(password)
            print(password)
            populatedPassword[:] = populatePassword(password)
            result.append(0)

        if event[0] == 'authorize':

            if event[1] == realHash:
                result.append(1)
            elif event[1] in populatedPassword:
               result.append(1)
            else:
                result.append(0)

    return result


if __name__ == '__main__':
    print(authEvents(["setPassword", "AAA"]))