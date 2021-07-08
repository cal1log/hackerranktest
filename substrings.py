#!/usr/bin/env python3

def count_substring(string, sub_string):
    count = 0
    match = 0
    if len(string) >= len(sub_string):
        for i in range(0, len(string) - len(sub_string) + 1):            
            for j in range(0, len(sub_string)):
                if string[i + j] == sub_string[j]:
                    count += 1            
            if count == len(sub_string):
                match += 1
            count = 0
    return match

if __name__ == '__main__':    
    
    x = input("type a string\n")
    y = input("type a substring to find inside the first string\n")
    print(count_substring(x, y))