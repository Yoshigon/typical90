import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

for _ in range(Q):
    tmp = int(input())
    idx = bisect.bisect_left(A, tmp)
    if idx == 0:
        print(A[0] - tmp)
    elif idx == N:
        print(tmp - A[N-1])
    else:
        print(min(A[idx] - tmp, tmp - A[idx-1]))
