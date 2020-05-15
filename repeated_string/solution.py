#!/bin/python3

import math

def isRepeated(string, num):
  string_length = len(string)

  counter = int((string_length * math.ceil(num/string_length))/string_length)
  repeated_string = string * counter

  return repeated_string[:n].count('a')

if __name__ == '__main__':
  s = 'aba'
  n = 10

  result = isRepeated(s, n)
  print(result)