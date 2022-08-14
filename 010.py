N = int(input())
class_one = [0] * (N+1)
class_two = [0] * (N+1)

for i in range(1, N+1):
    c, p = map(int, input().split())
    if c == 1:
        class_one[i] = p
    else:
        class_two[i] = p

for i in range(N):
    class_one[i+1] += class_one[i]
    class_two[i+1] += class_two[i]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(class_one[r] - class_one[l-1], class_two[r] - class_two[l-1])
