#!/bin/python3

import math
import os
import random
import re
import sys



def countSwaps(our_list):
    
    counter = 0
    for i in range(len(our_list)):
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                counter += 1
        
    return counter


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    print(countSwaps(a))