from itertools import permutations
N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
bad_relations = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad_relations[x].add(y)
    bad_relations[y].add(x)

ans = 10001

for p in permutations(range(N)):
    flag = 0
    tmp = 0
    for i in range(N-1):
        if p[i] in bad_relations[p[i+1]]:
            flag = 1
            break
    if flag:
        continue
    else:
        for i in range(N):
            tmp += time[p[i]][i]
        ans = min(ans, tmp)

if ans == 10001:
    print(-1)
else:
    print(ans)
