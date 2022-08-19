N = int(input())
grid = [[0] * 1001 for _ in range(1001)]
area = {key: 0 for key in range(N+1)}

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    grid[lx][ly] += 1
    grid[lx][ry] -= 1
    grid[rx][ly] -= 1
    grid[rx][ry] += 1

for i in range(1001):
    for j in range(1000):
        grid[i][j+1] += grid[i][j]

for i in range(1000):
    for j in range(1001):
        grid[i+1][j] += grid[i][j]

for i in range(1001):
    for j in range(1001):
        area[grid[i][j]] += 1

for k in range(1, N+1):
    print(area[k])
