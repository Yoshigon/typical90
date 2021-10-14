N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range(N):
    count += abs(A[i]-B[i])

if count > K:
    print('No')
elif (count-K) % 2 == 0:
    print('Yes')
else:
    print('No')
