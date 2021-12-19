N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    tmp = A[i]
                    num = [A[j], A[k], A[l], A[m]]
                    for p in range(4):
                        tmp *= num[p]
                        tmp %= P
                    if tmp == Q:
                        count += 1
print(count)
