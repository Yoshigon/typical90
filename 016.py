N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
ans = 10000

for i in range(10000):
    tmp1 = coins[0] * i
    if tmp1 > N:
        break
    for j in range(10000):
        tmp2 = coins[0] * i + coins[1] * j
        if tmp2 > N:
            break
        if (N - tmp2) % coins[2] == 0:
            ans = min(ans, i + j + (N - tmp2) // coins[2])

print(ans)
