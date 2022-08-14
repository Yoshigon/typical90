N = int(input())
S = input()
MOD = 10 ** 9 + 7

dp = [[0] * N for _ in range(7)]
if S[0] == 'a':
    dp[0][0] = 1

for i in range(1, N):
    for j in range(7):
        dp[j][i] = dp[j][i-1]
        dp[j][i] %= MOD
    if S[i] == 'a':
        dp[0][i] += 1
    elif S[i] == 't':
        dp[1][i] += dp[0][i-1]
    elif S[i] == 'c':
        dp[2][i] += dp[1][i-1]
    elif S[i] == 'o':
        dp[3][i] += dp[2][i-1]
    elif S[i] == 'd':
        dp[4][i] += dp[3][i-1]
    elif S[i] == 'e':
        dp[5][i] += dp[4][i-1]
    elif S[i] == 'r':
        dp[6][i] += dp[5][i-1]

print(dp[6][N-1] % MOD)
