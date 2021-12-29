N = int(input())
S = input()

last_circle = -1
last_cross = -1
ans = 0

for i in range(N):
    if S[i] == 'o':
        last_circle = i
        if last_cross == -1:
            continue
        ans += last_cross + 1

    else:
        last_cross = i
        if last_circle == -1:
            continue
        ans += last_circle + 1

print(ans)
