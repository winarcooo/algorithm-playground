import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        return "No"

    counter = 0
    for n in note:
        if n in magazine:
            counter += 1
            magazine.remove(n)
    
    if counter == len(note):
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
