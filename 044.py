N, Q = map(int, input().split())
A = list(map(int, input().split()))
shift = 0

for _ in range(Q):
    t, x, y = map(int, input().split())
    x += N - (shift+1)
    y += N - (shift+1)
    x %= N
    y %= N

    if t == 1:
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp
    elif t == 2:
        shift += 1
    elif t == 3:
        print(A[x])
