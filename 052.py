N = int(input())
ans = 1
MOD = 10 ** 9 + 7

for _ in range(N):
    dice = list(map(int, input().split()))
    ans *= sum(dice)
    ans %= MOD

print(ans)
