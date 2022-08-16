import math
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    E = int(input())
    y = -L/2 * math.sin(2 * math.pi * E / T)
    z = L/2 * (1 - math.cos(2 * math.pi * E / T))
    print(math.degrees(math.atan(z / X ** 2 + (Y - y) ** 2) ** (1/2)))
