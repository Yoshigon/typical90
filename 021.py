from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <n>: 頂点サイズ, <g>: 順方向の有向グラフ, <rg>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)


def scc(n, g, rg):
    order = []
    used = [0] * n
    group = [None] * n

    def dfs(start):
        used[start] = 1
        for t in g[start]:
            if not used[t]:
                dfs(t)
        order.append(start)

    def rdfs(start, col):
        group[start] = col
        used[start] = 1
        for t in rg[start]:
            if not used[t]:
                rdfs(t, col)
    for i in range(n):
        if not used[i]:
            dfs(i)
    used = [0] * n
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


N, M = map(int, input().split())
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    RG[b-1].append(a-1)

num_groups, group_labels = scc(N, G, RG)
ans = 0
group_members = defaultdict(lambda: 0)

for i in range(N):
    group_members[group_labels[i]] += 1

for val in group_members.values():
    ans += val * (val-1) // 2

print(ans)
