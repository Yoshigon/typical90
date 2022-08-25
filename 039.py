import sys
sys.setrecursionlimit(10**6)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

dp = [0] * N
ans = 0


def dfs(now: int, pre: int):
    global ans
    for node in edges[now]:
        if node != pre:
            dfs(node, now)
    dp[now] += 1
    if pre != -1:
        dp[pre] += dp[now]
    ans += dp[now] * (N - dp[now])


dfs(0, -1)
print(ans)
