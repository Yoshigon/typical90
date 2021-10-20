from itertools import permutations

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
bad_relation = {key: {} for key in range(N)}
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad_relation[x][y] = 1
    bad_relation[y][x] = 1
ans = 10 ** 5

for v in permutations(range(N)):
    flag = 0
    for i in range(N-1):
        if v[i+1] in bad_relation[v[i]]:
            flag = 1
            break
    if flag:
        continue

    tmp = 0
    for i in range(N):
        tmp += time[v[i]][i]
    ans = min(ans, tmp)

if ans != 10 ** 5:
    print(ans)
else:
    print(-1)
