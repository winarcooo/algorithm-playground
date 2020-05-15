#!/bin/python3

if __name__ == '__main__':
  n = int(input())
  integer_list = map(int, input().split())

list_temp = list()
for i in integer_list:
  list_temp.append(i)

integer_tumple = tuple(list_temp)

print(hash(integer_tumple))
