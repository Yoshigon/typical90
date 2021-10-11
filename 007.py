import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

for _ in range(Q):
    tmp = int(input())
    idx = bisect.bisect_left(A, tmp)
    if idx == 0:
        print(abs(tmp - A[0]))
    elif idx == N:
        print(abs(tmp - A[N-1]))
    else:
        print(min(abs(tmp - A[idx]), abs(tmp - A[idx-1])))
