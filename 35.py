import math

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x & 1 == 0:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
       if x % i == 0:
           return False
    return True

def left_rotate(x, n):
    return x[n:] + x[:n]

def is_clr_prime(x, primes):
    x_str = str(x)
    x_len = len(x_str)
    numbers = [int(left_rotate(x_str, i)) for i in range(x_len)]
    if all([number in primes for number in numbers]):
        return True, numbers
    else:
        return False, numbers

primes = [i for i in range(2, 1000000) if is_prime(i)]

primes_dict = {}
result = {}
for prime in primes:
    primes_dict[prime] = 1

for i in primes:
    ok, numbers = is_clr_prime(i, primes_dict)
    if ok:
        result[numbers[0]] = numbers
    else:
        for number in numbers:
            if number in primes_dict:
                del primes_dict[number]
print len(result)
