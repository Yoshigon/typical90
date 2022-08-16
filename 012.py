from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


H, W = map(int, input().split())
Q = int(input())
red = {}
ans = []
uf = UnionFind(H*W)

for _ in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        r = tmp[1]-1
        c = tmp[2]-1
        red[r*W+c] = 1
        if (r-1)*W+c in red:  # (r-1, c)
            uf.union(W*r+c, W*(r-1)+c)
        if (r+1)*W+c in red:  # (r+1, c)
            uf.union(W*r+c, W*(r+1)+c)
        if 0 < c:
            if W*r+c-1 in red:  # (r, c-1)
                uf.union(W*r+c, W*r+c-1)
        if c < W-1:
            if W*r+c+1 in red:  # (r, c+1)
                uf.union(W*r+c, W*r+c+1)
    elif tmp[0] == 2:
        a = (tmp[1]-1) * W + tmp[2]-1
        b = (tmp[3]-1) * W + tmp[4]-1
        if a not in red:
            ans.append('No')
        elif uf.same(a, b):
            ans.append('Yes')
        else:
            ans.append('No')

print(*ans, sep='\n')
