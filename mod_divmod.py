#!/usr/bin/env python3

x = float(input())
y = float(input())
div = 0

if x != 0: 
    div = int(x / y)
    
divmod = int(x % y)

print(div)
print(divmod)
print('({}, {})'.format(div, divmod))