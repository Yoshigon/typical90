L, R = map(int, input().split())
MOD = 10 ** 9 + 7
ans = 0

for i in range(20):  # i+1桁の数が何個含まれているか調べる
    right = 10 ** (i + 1) - 1
    if 10 ** i > R:
        break
    if right < L:
        continue
    tmp = (10 ** i + right) * (right - 10 ** i + 1) // 2
    if 10 ** i < L:
        tmp -= (10 ** i + (L-1)) * ((L-1) - 10 ** i + 1) // 2  # 区間の左端
    if right > R:
        tmp -= ((R+1) + right) * (right - (R+1) + 1) // 2  # 区間の右端
    ans += tmp * (i + 1)
    ans %= MOD

print(ans)
