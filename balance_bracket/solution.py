#!/bin/python3

import math
import os
import random
import re
import sys

def isPair(open, close):
  if open == "(" and close == ")":
    return True
  elif open == "{" and close == "}":
    return True
  elif open == "[" and close == "]":
    return True
  return False

def isOpen(param):
  if param in ("(", "{", "["):
    return True
  return False

def isClose(param):
  if param in (")", "}", "]"):
    return True
  return False
  

# Complete the isBalanced function below.
def isBalanced(string):
  temporary = []
  brackets = list(string)

  for item in brackets:
    print(isClose(item))
    if len(temporary) == 0 and isClose(item):
      return "NO"

    if isOpen(item):
      temporary.append(item)
    
    if isClose(item):
      prevBracket = temporary[-1]
      if isPair(prevBracket, item):
        temporary.pop()
      else:
        return "NO"

  if len(temporary) == 0:
    return "YES"
  
  return "NO"


if __name__ == '__main__':
  input0 = "{(([])[])[]]}"
  input1 = "{[()]}"
  input2 = "[])"

  result = isBalanced(input2)
  print(result)