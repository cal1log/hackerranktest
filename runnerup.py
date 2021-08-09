#!/usr/bin/env python3


n = int(input())
arr = map(int, input().split())
arr = list(arr)
arr.sort()
x = arr[len(arr) - 1]
for i in range(len(arr) - 1, -1, -1):    
    if arr[i] < x:
        print(arr[i])
        break