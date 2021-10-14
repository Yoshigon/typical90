from collections import deque

N = int(input())
edges = [[] for _ in range(N)]
color_zero = []
color_one = []
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)


que = deque([(0, 0)])
visited = {}
while que:
    now, color = que.popleft()
    if now not in visited:
        visited[now] = 1
        if color == 0:
            color_zero.append(now+1)
        else:
            color_one.append(now+1)
        for node in edges[now]:
            if node not in visited:
                que.append((node, (color-1)*(-1)))

if len(color_zero) < len(color_one):
    color_one.sort()
    print(*color_one[:(N//2)])
else:
    color_zero.sort()
    print(*color_zero[:(N//2)])
