N, K = map(int, input().split())
scores = []
for _ in range(N):
    a, b = map(int, input().split())
    scores.append(a-b)
    scores.append(b)

scores.sort(reverse=True)
print(sum(scores[:K]))
