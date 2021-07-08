#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):    
    l = []
    x = ''
    for i in range(0, len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            if i == 0 or ord(s[i - 1]) == 32:                
                l.append(chr(ord(s[i]) - 32))            
            else:            
                l.append(s[i])
        else:            
            l.append(s[i])        
    for i in l:
        x += i
    return x  

if __name__ == '__main__':
    '''fptr = open(os.environ['OUTPUT_PATH'], 'w')'''

    s = input()

    result = solve(s)

    print(result)

    '''fptr.write(result + '\n')

    fptr.close()'''