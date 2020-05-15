#!/bin/python3

def swap_case(string):
  swapped_list = map(swap_letter, string)
  result = list(swapped_list)

  print(''.join(result))

def swap_letter(letter):

  if letter == ' ':
    return ' '

  if letter.isupper() and letter.isalpha():
    return letter.lower()
  
  if letter.islower() and letter.isalpha():
    return letter.upper()
  
  return letter
      

if __name__ == '__main__':
  # s = input()
  # result = swap_case(s)
  # print(input().swap_letter())

  test1 = 'Hello World!'

  swap_case(test1)