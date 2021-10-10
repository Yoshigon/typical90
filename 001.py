N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A_mevius = [A[0]]
for i in range(N-1):
    A_mevius.append(A[i+1] - A[i])
A_mevius.append(L-A[-1])


def check_possible(length: int, cut: list):
    tmp = 0
    cnt = 0
    for c in cut:
        tmp += c
        if tmp >= length:
            tmp = 0
            cnt += 1
            if cnt == K+1:
                return True

    return False


left = 1
right = (L // (K+1)) + 1

while right - left > 1:
    mid = (left + right) // 2
    if check_possible(mid, A_mevius):
        left = mid
    else:
        right = mid

print(left)
