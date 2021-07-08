#!/usr/bin/env python3

if __name__ == '__main__':
    N = int(input())
    l = [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]

    for i in range(0, N):
        com = []
        com = str(input()).split()                
        if com[0] == "append":
            l.append(int(com[1]))            
        if com[0] == "print":
            print(l)
        if com[0] == "sort":
            if len(l) > 0:
                l.sort()
        if com[0] == "reverse":
            if len(l) > 0:
                l.reverse()
        if com[0] == "pop":
            if len(l) > 0:
                l.pop()
        if com[0] == "remove":            
            for j in l:
                if int(com[1]) == j:
                    l.remove(int(com[1]))
                    break
        if com[0] == "insert":                 
            l.insert(int(com[1]), int(com[2]))