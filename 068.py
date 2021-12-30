from collections import defaultdict, deque


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


N = int(input())
Q = int(input())
events = []
ambiguous = {}
relations = [[] for _ in range(N)]


uf = UnionFind(N)
for i in range(Q):
    t, x, y, v = map(int, input().split())
    x -= 1
    y -= 1
    events.append([t, x, y, v])
    if t == 0:
        uf.union(x, y)
        relations[x].append([y, v])
        relations[y].append([x, v])
    elif t == 1:
        if not uf.same(x, y):
            ambiguous[i] = 1

relative_val = [0] * N
discovered = {}
for i in range(N):
    if i not in discovered:
        que = deque([[i, 0]])  # i=0と仮定
        relative_val[i] = 0
        discovered[i] = 1
        while que:
            idx, val = que.pop()
            for clue in relations[idx]:
                idx_y = clue[0]
                val_y = clue[1] - val
                if idx_y not in discovered:
                    discovered[idx_y] = 1
                    relative_val[idx_y] = val_y
                    que.append([idx_y, val_y])

for i in range(Q):
    if events[i][0] == 1:
        if i in ambiguous:
            print('Ambiguous')
        else:
            x = events[i][1]
            y = events[i][2]
            v = events[i][3]
            adjust = v - relative_val[x]
            if (x-y) % 2 != 0:
                print(relative_val[y] - adjust)
            else:
                print(relative_val[y] + adjust)
