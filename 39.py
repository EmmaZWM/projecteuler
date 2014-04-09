def is_right_triangle(a, b, c):
    if a ==0 or b ==0 or c==0:
        return False
    return (a*a == b*b + c*c) or (c*c == a*a + b *b) or (b*b == a*a + c*c)

def count(p):
    cnt = 0
    for i in range(1,p/2):
        for j in range(i, p/2):
            k = p - i - j
            if k < j:
                continue
            if is_right_triangle(i, j, k):
                cnt += 1
    return cnt

result = []
for p in range(3, 1000):
    result.append(count(p))

print result.index(max(result))+3, max(result)
