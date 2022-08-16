N = int(input())
jobs = [list(map(int, input().split())) for _ in range(N)]
jobs.sort()
dp = [0] * 5001

for d, c, s in jobs:
    for day in range(d-c, -1, -1):
        dp[day+c] = max(dp[day+c], dp[day]+s)

print(max(dp))
