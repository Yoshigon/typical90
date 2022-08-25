N, L = map(int, input().split())
dp = [1] + [0] * N
MOD = 10 ** 9 + 7

for i in range(N):
    dp[i] %= MOD
    dp[i+1] += dp[i]
    if i+L < N+1:
        dp[i+L] += dp[i]

print(dp[-1] % MOD)
