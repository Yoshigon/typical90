from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
maze = [input() for _ in range(H)]
cost = [[10**6] * W for _ in range(H)]

que = deque([(0, -1, rs-1, cs-1)])
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

while que:
    c, d, x, y = que.popleft()
    if x == rt-1 and y == ct-1:
        print(c-1)
        exit()
    for i in range(4):
        next_x, next_y = x + directions[i][0], y + directions[i][1]
        if 0 <= next_x <= H-1 and 0 <= next_y <= W-1:
            if maze[next_x][next_y] == '.':
                if i == d:
                    if cost[next_x][next_y] >= c:
                        cost[next_x][next_y] = c
                        que.appendleft((c, i, next_x, next_y))
                else:
                    if cost[next_x][next_y] >= c+1:
                        cost[next_x][next_y] = c+1
                        que.append((c+1, i, next_x, next_y))
