import math


def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            count = 0
            while tmp % i == 0:
                count += 1
                tmp //= i
            arr.append([i, count])
    if tmp != 1:
        arr.append([tmp, 1])
    if not arr:
        arr.append([n, 1])
    return arr


N = int(input())
factors = factorization(N)
count = 0
for i in range(len(factors)):
    count += factors[i][1]

print(math.ceil(math.log(count, 2)))
