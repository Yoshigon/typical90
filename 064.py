N, Q = map(int, input().split())
A = list(map(int, input().split()))
dif = [0]
inconvenience = 0

for i in range(1, N):
    dif.append(A[i] - A[i - 1])
    inconvenience += abs(A[i] - A[i - 1])

for _ in range(Q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1

    if l > 0:
        inconvenience += abs(dif[l] + v) - abs(dif[l])
        dif[l] += v
    if r < N-1:
        inconvenience += abs(dif[r+1] - v) - abs(dif[r+1])
        dif[r+1] -= v

    print(inconvenience)
