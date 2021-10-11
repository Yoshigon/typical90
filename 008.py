N = int(input())
S = input()
MOD = 10 ** 9 + 7
goal = 'atcoder'
dp = [[0] * 8 for _ in range(N)]
dp[0][0] = 1
if S[0] == 'a':
    dp[0][1] = 1

for i in range(1, N):
    for j in range(8):
        dp[i][j] += dp[i-1][j]
        if j == 0:
            continue
        if S[i] == goal[j-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= MOD

print(dp[-1][-1])
