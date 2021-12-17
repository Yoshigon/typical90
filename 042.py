K = int(input())
if K % 9 != 0:
    print(0)
    exit()

MOD = 10 ** 9 + 7
dp = [0] * (K+10)  # 各けたの和がiとなる数の個数はdp[i]
dp[0] = 1

for i in range(K):
    for j in range(1, 10):
        dp[i+j] += dp[i]
        dp[i+j] %= MOD

print(dp[K])
