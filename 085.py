K = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def make_divisors2(n, m):  # nの約数のうち、m以上の約数のみ求める
    lower_divisors, upper_divisors = [], []
    i = m
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


ans = 0
factors = make_divisors(K)

for a in factors:
    if a ** 3 > K:  # aは最小
        break
    factors2 = make_divisors2(K // a, a)  # (K // a) の約数のうち、a以上のもの
    num_factors = len(factors2)
    if num_factors % 2 == 0:
        ans += num_factors // 2
    else:
        ans += (num_factors+1) // 2

print(ans)
