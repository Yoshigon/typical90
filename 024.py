N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dif = 0
for i in range(N):
    dif += abs(A[i]-B[i])

if dif > K:
    print('No')
elif (dif - K) % 2 != 0:
    print('No')
else:
    print('Yes')
