N = int(input())
ranges = [list(map(int, input().split())) for _ in range(N)]
range_widths = []
for r in ranges:
    range_widths.append(r[1] - r[0] + 1)

exp = [0] * N  # exp[i]: i番目の数を追加した時の転倒数の期待値

for i in range(1, N):  # i番目に追加する数字
    l1, r1 = ranges[i]
    for j in range(i):  # 0~(i-1)番目に追加した数字
        tmp_exp = 0
        l0, r0 = ranges[j]
        for num in range(l1, r1 + 1):
            if num < l0:
                tmp_exp += r0 - l0 + 1
            elif l0 <= num < r0:
                tmp_exp += r0 - num
        tmp_exp /= range_widths[i] * range_widths[j]
        exp[i] += tmp_exp

print(sum(exp))
