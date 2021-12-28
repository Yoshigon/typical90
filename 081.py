N, K = map(int, input().split())
data = [[0] * 5000 for _ in range(5000)]

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    data[a][b] += 1

for i in range(5000):
    for j in range(1, 5000):
        data[i][j] += data[i][j-1]

for i in range(1, 5000):
    for j in range(5000):
        data[i][j] += data[i-1][j]

ans = 1

for a in range(5000):
    for b in range(5000):
        lx = a
        ly = b
        rx = min(a + K, 4999)
        ry = min(b + K, 4999)
        tmp = data[ry][rx]
        if lx > 0:
            tmp -= data[ry][lx-1]
        if ly > 0:
            tmp -= data[ly-1][rx]
        if lx > 0 and ly > 0:
            tmp += data[ly-1][lx-1]

        ans = max(ans, tmp)

print(ans)
