N = int(input())
A = list(map(int, input().split()))
dp = [[10 ** 9] * 2 * N for _ in range(2*N-1)]
for i in range(2*N-1):
    dp[i][i+1] = abs(A[i] - A[i+1])

for interval in range(3, 2*N, 2):
    for i in range((2*N) - interval):
        j = i + interval
        dp[i][j] = min(dp[i][j], dp[i+1][j-1] + abs(A[i] - A[j]))
        for k in range(i+1, j, 2):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

print(dp[0][-1])
