from math import sqrt

def is_prime(_var):
    if _var < 2:
        return False
    if _var == 2:
        return True
    if _var & (_var-1)==0:
        return False
    for i in xrange(2, int(sqrt(_var)) +1):
        if _var % i == 0:
            return False
    return True

def left_truncate(x, n):
    return x[n:]

def right_trucate(x, n):
    return x[:-n]


count = 0
result = []
primes = {2:1,3:1,5:1,7:1}
x = 11
while count != 11:
    if not is_prime(x):
        x += 1
        continue
    primes[x] = 1
    x_str = str(x)
    x_len = len(x_str)
    left_truncators = [int(left_truncate(x_str, i)) for i in range(1, x_len)]
    right_trucators = [int(right_trucate(x_str, i)) for i in range(1, x_len)]
    if all([left in primes for left in left_truncators]) and all([right in primes for right in right_trucators]):
             count += 1
             result.append(x)
    x += 1
print sum(result)
