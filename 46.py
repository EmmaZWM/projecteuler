from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x & 1 == 0:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def gen_prime(x, y):
    result = []
    for i in range(x, y):
        if is_prime(i):
            result.append(i)
    return result

def is_odd_composition_number(x):
    if x & (x-1) == 0 or is_prime(x):
        return False
    return True

def is_two_square(x):
    if x & 1 != 0:
        return False
    square_extraction = sqrt(x/2)
    if square_extraction == int(square_extraction):
        return True
    return False

start = 3
primes = []
cur = 1
found = False
while True:
    found = False
    if is_odd_composition_number(start):
        primes += gen_prime(cur, start)
        l = len(primes)
        for i in range(l):
            if is_two_square(start - primes[i]):
                found = True
                break
        if not found:
            print start
            break
        cur = start
    start += 2
