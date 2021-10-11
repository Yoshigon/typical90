N, K = map(int, input().split())
S = input()
ans = ''
head = 0

tmp = 'z'
while len(ans) < K:
    for i in range(head, N - K + len(ans) + 1):
        if S[i] < tmp:
            head = i
            tmp = S[i]
    ans += tmp
    head += 1
    tmp = 'z'

print(ans)
