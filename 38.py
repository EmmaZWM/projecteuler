def is_pandigital_number(x):
    limit = 9
    i = 1
    x_str = str(x)
    x_len = len(x_str)
    cur = 0
    result = ''
    while cur < limit:
        y = str(i * x)
        result += y
        cur += len(y)
        i += 1

    if cur > limit:
        return False, result
    elif all([str(i) in result for i in range(1, 10)]):
        return True, result
    return False, result

for i in xrange(59876, 1, -1):
    ok, result = is_pandigital_number(i)
    if ok:
        print result
        break
