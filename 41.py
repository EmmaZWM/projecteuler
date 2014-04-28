import math

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x & (x-1) == 0:
        return False
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

def is_pandigital(x, len):
    return all(str(i) in x for i in range(1, len+1))

start = 7654321
while (start > 0):
    start_str = str(start)
    if is_prime(start):
        if is_pandigital(start_str,len(start_str) ):
            print start
            break
    start = start -1

