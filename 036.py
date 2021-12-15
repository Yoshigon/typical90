N, Q = map(int, input().split())
coordinates = [list(map(int, input().split())) for _ in range(N)]
x_45 = []
y_45 = []
for c in coordinates:
    x_45.append(c[0] + c[1])
    y_45.append(c[0] - c[1])


min_x_45 = sorted(x_45)[0]
max_x_45 = sorted(x_45)[-1]
min_y_45 = sorted(y_45)[0]
max_y_45 = sorted(y_45)[-1]

for _ in range(Q):
    q = int(input())-1
    x_q = x_45[q]
    y_q = y_45[q]
    ans = max(abs(x_q - min_x_45), abs(x_q - max_x_45), abs(y_q - min_y_45), abs(y_q - max_y_45))
    print(ans)
