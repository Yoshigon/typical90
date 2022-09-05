def get_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


N, K = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]
INF = 1 << 60
dp = [INF] * (1 << N)
dp[0] = 0
dist = [0] * (1 << N)

for i in range(N):
    for bit in range(1 << i):
        tmp_dist = dist[bit]
        for j in range(i):
            if (bit >> j) & 1:
                tmp_dist = max(tmp_dist, get_dist(points[i][0], points[i][1], points[j][0], points[j][1]))
        dist[bit | (1 << i)] = max(dist[bit | (1 << i)], tmp_dist)

dp = dist[:]
for _ in range(K - 1):
    for bit in range((1 << N) - 1, -1, -1):
        subset = bit
        while subset:
            dp[bit] = min(dp[bit], max(dp[subset ^ bit], dist[subset]))
            subset = (subset - 1) & bit

ans = dp[(1 << N) - 1]
print(ans)
