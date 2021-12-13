N, K = map(int, input().split())

num_with_k_prime_factors = {key: 0 for key in range(9)}
num_prime_factors = [0 for i in range(N+1)]  # 1からNの数がもつ素因数の数

for i in range(2, N+1):
    if num_prime_factors[i] == 0:  # 素数の場合
        for j in range(i, N+1, i):
            num_prime_factors[j] += 1

    if num_prime_factors[i] > 8:
        num_with_k_prime_factors[8] += 1
    else:
        num_with_k_prime_factors[num_prime_factors[i]] += 1

ans = 0
for k in range(K, 9):
    ans += num_with_k_prime_factors[k]

print(ans)
