import bisect

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

for i in range(N):
    edges[i].sort()

ans = 0

for i in range(N):
    idx = bisect.bisect_left(edges[i], i)
    if idx == 1:
        ans += 1

print(ans)
