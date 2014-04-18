facs = [1]
for i in range(1, 10):
    facs.append( facs[i-1] * i )

def is_digit_fac(n, facs):
    tmp = n
    if n < 10:
        return False
    multi = 0 
    while n != 0:
        multi += facs[n%10]
        n /= 10
    if multi == tmp:
        return True


result = 0
for i in range(10, 2540161):
    if is_digit_fac(i, facs):
        result += i

print result
