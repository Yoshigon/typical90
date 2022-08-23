N, Q = map(int, input().split())
coordinates = []
X = []  # x+y
Y = []  # x-y

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))
    X.append(x+y)
    Y.append(x-y)

X.sort()
Y.sort()

for i in range(Q):
    q = int(input())
    x, y = coordinates[q-1]
    print(max(x+y-X[0], -(x-y)+Y[-1], x-y-Y[0], -(x+y)+X[-1]))
