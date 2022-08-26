K = int(input())
MOD = 10**9+7

if K % 9 != 0:
    print(0)
    exit()

dp = [1] + [0] * (K+8)

for i in range(K):
    for j in range(1, 10):
        dp[i+j] += dp[i]
        dp[i+j] %= MOD

print(dp[K])
