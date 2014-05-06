import math
import types

def is_pentagon_number(x):
    n = (math.sqrt(1+ 24 * x) + 1)/6.0
    return n == int(n)

def solution():
    i = 1
    not_found = True
    while not_found:
        n = i * (3 * i - 1)/2
        for j in range(i-1, 0, -1):
            m = j * (3*j-1)/2
            if is_pentagon_number(m + n) and is_pentagon_number(n -m):
                not_found = False
                print n-m
                break
        i += 1

if __name__ == '__main__':
    print is_pentagon_number(1)
    solution()
    
