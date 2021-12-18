from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
grid = [input() for _ in range(H)]

cost = [[float("inf")] * W for i in range(H)]
cost[rs-1][cs-1] = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

que = deque([(rs-1, cs-1)])

while que:
    r, c = que.popleft()
    if r == rt-1 and c == ct-1:
        break
    for dh, dw in directions:
        nh, nw = r + dh, c + dw
        while 0 <= nh <= H-1 and 0 <= nw <= W-1 and grid[nh][nw] == "." and cost[nh][nw] > cost[r][c]:
            if cost[nh][nw] == float("inf"):
                que.append((nh, nw))
            cost[nh][nw] = cost[r][c] + 1
            nh += dh
            nw += dw

print(cost[rt-1][ct-1] - 1)
