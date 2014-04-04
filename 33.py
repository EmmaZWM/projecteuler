def gcd(a, b):
    while a != b:
        if a < b:
            t = a
            a = b
            b = t
        a = a - b
    return a

def non_trival(a, b):
    a1 = a/10
    a2 = a%10
    b1 = b/10
    b2 = b%10
    
    if a2 == 0 or b2 == 0:
        return False

    g = gcd(a,b)
    a0 = a/g
    b0 = b/g

    if a2 == b1:
        return (a1*1.0/b2 == a0*1.0/b0)
    if a1 == b2:
        return (a2*1.0/b1 == a0*1.0/b0)


print non_trival(75, 77)

p1 =  1
p2 = 1
for i in range(11, 99):
    for j in range(i+1, 100):
        if non_trival(i, j):
            print i, j
            p1 *= i
            p2 *= j
g = gcd(p1, p2)
print p2/g
    
