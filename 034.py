N, K = map(int, input().split())
A = list(map(int, input().split()))

num_count = {A[0]: 1}
head = 0
tail = 1
types = 1
ans = 1

while tail < N:
    tail += 1
    if A[tail-1] not in num_count:
        num_count[A[tail-1]] = 1
        types += 1
    elif num_count[A[tail-1]] == 0:
        num_count[A[tail-1]] = 1
        types += 1
    else:
        num_count[A[tail-1]] += 1
    while types > K:
        num_count[A[head]] -= 1
        if num_count[A[head]] == 0:
            types -= 1
        head += 1
    ans = max(ans, tail-head)

print(ans)
