N, Q = map(int, input().split())
A = list(map(int, input().split()))
shift = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        x_back = (x - shift) % N
        y_back = (y - shift) % N
        tmp = A[x_back-1]
        A[x_back-1] = A[y_back-1]
        A[y_back-1] = tmp
    elif t == 2:
        shift += 1
    elif t == 3:
        x_back = (x - shift) % N
        print(A[x_back-1])
