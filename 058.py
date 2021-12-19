N, K = map(int, input().split())


def button_A(x: int):
    y = 0
    for digit in str(x):
        y += int(digit)
    z = (x+y) % (10 ** 5)
    return z


num_dic = {N: 0}
sequence = [N]
num = N

for i in range(K):
    next_num = button_A(num)

    if next_num not in num_dic:
        num_dic[next_num] = i+1
        sequence.append(next_num)
        num = next_num
    else:
        idx = num_dic[next_num]  # idx以降を繰り返す
        rep = sequence[idx:]
        rem = K + 1 - idx
        rem %= len(rep)
        print(rep[rem-1])
        exit()

print(num)
