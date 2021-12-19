import bisect

N = int(input())
A = list(map(int, input().split()))
dp_increase = [1] * N
dp_decrease = [1] * N

LIS = [A[0]]
count = 1
for i in range(1, N):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
        count += 1
    else:
        LIS[bisect.bisect_left(LIS, A[i])] = A[i]
    dp_increase[i] = count

LDS = [A[-1]]
count = 1
for i in range(N-1, -1, -1):
    if A[i] > LDS[-1]:
        LDS.append(A[i])
        count += 1
    else:
        LDS[bisect.bisect_left(LDS, A[i])] = A[i]
    dp_decrease[i] = count

ans = 1
for i in range(N):
    ans = max(ans, dp_increase[i] + dp_decrease[i] - 1)

print(ans)
