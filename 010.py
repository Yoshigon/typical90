N = int(input())
score1 = [0] * N
score2 = [0] * N
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        score1[i] += p
    else:
        score2[i] += p

for i in range(1, N):
    score1[i] += score1[i-1]
    score2[i] += score2[i-1]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == 0:
        print(score1[r], score2[r])
    else:
        print(score1[r]-score1[l-1], score2[r]-score2[l-1])
