#!/usr/bin/env python3

def print_rangoli(size):
    if size > 0 and size < 27:
        l = []
        ll = []        
        lis = []        
        ch = 97
        flag = 0        
        t = ""
        
        ''' get the triangle right bottom '''
        for i in range(0, size):            
            if flag == 0:
                for j in range(0, size):
                    lis.append(str(chr(97 + j)))                        
            ch = ch + i
            for w in range(0, (size - 1) * 2 + 1):                                
                if w % 2 == 0 and str(chr(ch)) in lis:
                    ll.append(str(chr(ch)))
                    ch += 1                    
                else:
                    ll.append("-")
            ch = 97
            flag += 1                
            l.append(ll.copy())
            ll.clear()

        ''' insert the lines above the middle '''
        ll.append(l.copy())                
        flag = 0
        for j in range(len(ll[0]) - 1, 0, -1):            
            l.insert(flag, ll[0][j])
            flag += 1
        ll.clear()

        ''' reverse every row without middle element '''
        ll.append(l.copy())                
        flag = 0
        for j in range(0, len(ll)):
            for w in range(0, len(ll[j])):                            
                for x in range(len(ll[j][w]) - 1, 0, -1):
                    t += ll[j][w][x]                
                for x in range(0, len(ll[j][w])):
                    t += ll[j][w][x]                
                print(t)
                t = ""               
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)