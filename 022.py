import math
A, B, C = map(int, input().split())
gcd = math.gcd(A, math.gcd(B, C))
print(A // gcd + B // gcd + C // gcd - 3)
