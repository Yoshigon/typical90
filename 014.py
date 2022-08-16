N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

inconvenience = 0
for i in range(N):
    inconvenience += abs(A[i] - B[i])

print(inconvenience)
