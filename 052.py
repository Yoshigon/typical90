N = int(input())
MOD = 10 ** 9 + 7
ans = 1
for _ in range(N):
    dice = sum(list(map(int, input().split())))
    ans *= dice
    ans %= MOD
print(ans)
