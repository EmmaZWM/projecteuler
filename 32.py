import string

def pandigital( p_str ):
    product = string.atoi(p_str[-4:])
    for i in range(1, 4):
        multiplicand = string.atoi(p_str[0:i])
        multiplier = string.atoi(p_str[i:5])
        if multiplier * multiplicand == product:
            return product
    return False
def nextPermutation( p ):
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

if __name__ == "__main__":
  start = "123456789"
  data = []
  while start != False:
      product = pandigital(start)
      if product != None:
          data.append(product)
      start = nextPermutation(start)
  print sum(set(data))
