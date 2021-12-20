N, K = map(int, input().split())
MOD = 10 ** 9 + 7

if K == 1:
    if N == 1:
        print(1)
    else:
        print(0)
elif K == 2:
    if N <= 2:
        print(2)
    else:
        print(0)
elif K >= 3:
    if N == 1:
        print(K % MOD)
    elif N == 2:
        print((K * (K-1)) % MOD)
    elif N >= 3:
        ans = K * (K-1) * pow(K-2, N-2, MOD)
        ans %= MOD
        print(ans)
