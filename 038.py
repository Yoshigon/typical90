import math
A, B = map(int, input().split())

gcd = math.gcd(A, B)
lcm = A // gcd * B
if lcm <= 10 ** 18:
    print(lcm)
else:
    print('Large')
