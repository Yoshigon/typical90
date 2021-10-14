N = int(input())
grid = [[0] * 1002 for _ in range(1002)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())

    grid[ly][lx] += 1
    grid[ly][rx] -= 1
    grid[ry][lx] -= 1
    grid[ry][rx] += 1

for i in range(1002):
    for j in range(1, 1002):
        grid[i][j] += grid[i][j-1]

for j in range(1002):
    for i in range(1, 1002):
        grid[i][j] += grid[i-1][j]

dic = {key: 0 for key in range(N+1)}
for i in range(1002):
    for j in range(1002):
        dic[grid[i][j]] += 1

for k in range(1, N+1):
    print(dic[k])
