def segfunc(x, y):
    return max(x, y)


class LazySegTreeRUQ:
    def __init__(self, init_val, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def get_index(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l&-l).bit_length()
        rm = r >> (r&-r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v

    def update(self, l, r, x):
        ids = self.get_index(l,r)
        self.propagates(*self.get_index(l,r))
        l += self.num
        r += self.num
        while l < r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def query(self, l, r):
        ids = self.get_index(l,r)
        self.propagates(*self.get_index(l, r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l&1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


W, N = map(int, input().split())
st = LazySegTreeRUQ([0]*(W+1), 0)
for _ in range(N):
    l, r = map(int, input().split())
    height = st.query(l, r+1)
    st.update(l, r+1, height+1)
    print(height+1)
