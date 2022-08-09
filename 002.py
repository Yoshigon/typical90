N = int(input())


def generate_parentheses_set(p: str, length: int, head: int, tail: int):
    if len(p) == length:
        if head == tail:
            head_count = 0
            tail_count = 0
            flag = 1
            for i in range(length):
                if p[i] == '(':
                    head_count += 1
                else:
                    tail_count += 1
                if head_count < tail_count:
                    flag = 0
                    break
            if flag:
                print(p)
    else:
        generate_parentheses_set(p+'(', length, head+1, tail)
        generate_parentheses_set(p+')', length, head, tail+1)


if N % 2 == 1:
    exit()
else:
    generate_parentheses_set('', N, 0, 0)
