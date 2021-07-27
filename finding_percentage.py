#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    n = 0    
    for num in student_marks[query_name]:
        n += num
    n = n / len(student_marks[query_name])
    print("{0:.2f}".format(n))
