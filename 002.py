N = int(input())
if N % 2 != 0:
    exit()


def generate_sequence(head: int, tail: int, tmp: str):
    if head > 0:
        generate_sequence(head-1, tail, tmp+'(')
    if tail > 0 and (head < tail):
        generate_sequence(head, tail-1, tmp+')')
    else:
        if len(tmp) == N:
            print(tmp)


generate_sequence(N//2, N//2, '')
