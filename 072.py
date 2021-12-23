import sys
import copy
sys.setrecursionlimit(10 ** 5)

H, W = map(int, input().split())
GRID = [input() for _ in range(H)]
ans = -1
direction = ((0, 1), (1, 0), (-1, 0), (0, -1))


def find_loop(start_x: int, start_y: int, visited: dict):
    global ans
    for d in direction:
        next_x = start_x + d[0]
        next_y = start_y + d[1]
        if 0 <= next_x <= W-1 and 0 <= next_y <= H-1:
            if GRID[next_y][next_x] == '.':
                if (next_y, next_x) not in visited:
                    tmp_visited = copy.deepcopy(visited)
                    tmp_visited[(next_y, next_x)] = 1
                    find_loop(next_x, next_y, tmp_visited)
                else:
                    if visited[(next_y, next_x)] == 10:
                        if len(visited) > 2:
                            ans = max(ans, len(visited))


for i in range(H):
    for j in range(W):
        find_loop(j, i, {(i, j): 10})

print(ans)
