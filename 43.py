import string

def next_permutation( p ):
    a = len(p) - 2
    while a >=0 and p[a] >= p[a+1]:
        a -= 1
    if a == -1:
        return False
    b = len(p) - 1
    while p[b] <= p[a]:
        b -= 1
    l = list(p)
    t = l[a]
    l[a]=l[b]
    l[b] = t

    i = a +1
    j = len(p) - 1
    while i < j:
        t = l[i]
        l[i]=l[j]
        l[j]=t
        i += 1
        j -= 1
    return ''.join(l)

start_str = "0123456789"
sum = 0
while start_str:
    start = [int(i) for i in start_str]
    start_int =string.atoi(start_str)
    start_str = next_permutation(start_str)
    
    #d2d3d4 is divided by 2
    if start[3] & 1 != 0:
        continue

    #d3d4d5 is divided by 3
    if (start[2] + start[3] + start[4]) %3 != 0:
        continue

    #d4d5d6 is divided by 5
    if (start[5] != 0) and (start[5] != 5):
        continue

    #d5d6d7 is divided by 7
    if (start[4]*100 + start[5]*10 + start[6]) % 7 != 0:
        continue

    #d6d7d8
    if (start[5] + start[7] - start[6]) % 11 != 0:
        continue

    #d7d8d9
    if (start[6] * 100 + start[7] * 10 + start[8]) %13 !=0:
        continue

    if (start[7] * 100 + start[8] * 10 + start[9] ) % 17 !=0:
        continue
    sum += start_int

print sum
