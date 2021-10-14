import sys
sys.setrecursionlimit(10 ** 6)


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


# 縮約後のグラフを構築
def construct(n, g, label, group):
    g0 = [set() for i in range(label)]
    gp = [[] for i in range(label)]
    for v in range(n):
        lbs = group[v]
        for w in g[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            g0[lbs].add(lbt)
        gp[lbs].append(v)
    return g0, gp


N, M = map(int, input().split())
edge = [[] for _ in range(N)]
reversed_edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    reversed_edge[b].append(a)

label, group = scc(N, edge, reversed_edge)
G0, GP = construct(N, edge, label, group)

ans = 0
for g in GP:
    ans += len(g) * (len(g)-1) // 2

print(ans)
