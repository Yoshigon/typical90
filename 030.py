N, K = map(int, input().split())
num_p_factors = [0] * (10**7+1)
ans = 0

for i in range(2, N+1):
    if num_p_factors[i] == 0:
        for j in range(i, N+1, i):
            num_p_factors[j] += 1
            if num_p_factors[j] == K:
                ans += 1

print(ans)
