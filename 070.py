N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

ideal_x = X[N//2]
ideal_y = Y[N//2]

ans = 0

for i in range(N):
    ans += abs(X[i] - ideal_x)
    ans += abs(Y[i] - ideal_y)

print(ans)
