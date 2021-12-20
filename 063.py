from itertools import combinations
from collections import defaultdict

H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

ans = 1
for i in range(1, H+1):  # 何行選ぶか
    for rows in combinations(range(H), i):  # どの行を選ぶか
        tmp_dic = defaultdict(lambda: 0)
        for j in range(W):  # 選んだ行について、全て同じ値の列を、値ごとにカウント
            judge_by_col = set()
            for r in rows:
                judge_by_col.add(grid[r][j])
            if len(judge_by_col) == 1:  # 列jの値は全て同じ
                tmp_dic[grid[rows[0]][j]] += i

        if tmp_dic:
            num_frequent_value = sorted(tmp_dic.values())[-1]
            ans = max(ans, num_frequent_value)

print(ans)
