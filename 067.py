N, K = map(int, input().split())


def base8_to_base10(num: int):
    num_base10 = 0
    num_digits = len(str(num))
    for i in range(-1, -1-num_digits, -1):
        num_base10 += 8 ** (-i-1) * int(str(num)[i])
    return num_base10


def base10_to_base9(num: int):
    num_base9 = ''
    digit_base9 = 1
    while 9 ** digit_base9 - 1 < num:
        digit_base9 += 1

    for d in range(digit_base9, 0, -1):
        tmp = num // (9 ** (d-1))
        num = num % (9 ** (d-1))
        num_base9 += str(tmp)
    return int(num_base9)


def convert_8_to_5(num: int):
    ret = ''
    for n in str(num):
        if n == '8':
            ret += '5'
        else:
            ret += n
    return ret


ans = N
for _ in range(K):
    ans = base8_to_base10(ans)
    ans = base10_to_base9(ans)
    ans = convert_8_to_5(ans)

print(ans)
