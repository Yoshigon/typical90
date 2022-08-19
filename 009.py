import math
import bisect

N = int(input())
coordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

ans = 0
for i in range(N):
    ax, ay = coordinates[i]
    angles = []
    for j in range(N):
        if i == j:
            continue
        angles.append(math.degrees(math.atan2(coordinates[j][0]-ax, coordinates[j][1]-ay)))
    angles.sort()

    for a in angles:
        idx = bisect.bisect_left(angles, (a+180) % 360)
        if idx == 0 or idx == N-1:
            angle_one = min(abs(a-angles[0]), 360-abs(a-angles[0]))
            angle_two = min(abs(a-angles[N-2]), 360-abs(a-angles[N-2]))
        else:
            angle_one = min(abs(a-angles[idx]), 360-abs(a-angles[idx]))
            angle_two = min(abs(a-angles[idx-1]), 360-abs(a-angles[idx-1]))
        ans = max(ans, angle_one, angle_two)

print(ans)
