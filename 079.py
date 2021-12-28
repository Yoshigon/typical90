H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

cnt = 0

for h in range(H-1):
    for w in range(W-1):
        dif = B[h][w] - A[h][w]
        A[h][w] += dif
        A[h][w+1] += dif
        A[h+1][w] += dif
        A[h+1][w+1] += dif
        cnt += abs(dif)

for h in range(H):
    for w in range(W):
        if A[h][w] != B[h][w]:
            print('No')
            exit()

print('Yes')
print(cnt)
