#!/usr/bin/env python3

def swap_case(s):    
    if len(s) > 0:        
        s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input('type a string\n')
    print(swap_case(s))