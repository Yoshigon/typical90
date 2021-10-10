H, W = map(int, input().split())
grid = []
row_sum = []
col_sum = [0] * W
for h in range(H):
    tmp = list(map(int, input().split()))
    grid.append(tmp)
    row_sum.append(sum(tmp))
    for w in range(W):
        col_sum[w] += tmp[w]

for i in range(H):
    tmp = []
    for j in range(W):
        tmp.append(row_sum[i] + col_sum[j] - grid[i][j])
    print(*tmp)
