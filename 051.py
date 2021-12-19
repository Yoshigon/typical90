from itertools import combinations
import bisect

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

group1 = A[:N//2]
group2 = A[N//2:]

ans = 0

for k in range(K+1):  # group1からk個選ぶ
    if k > N // 2:
        break
    if K - k > (N - N // 2):
        continue
    g1 = []
    g2 = []
    for v in combinations(group1, k):
        g1.append(sum(v))
    for v in combinations(group2, K-k):
        g2.append(sum(v))

    if not g1:
        g1.append(0)
    if not g2:
        g2.append(0)
    g1.sort()
    g2.sort()

    for g in g1:  # g2から(P-g)円以下の物を探す
        idx = bisect.bisect_right(g2, P-g)
        ans += idx

print(ans)
