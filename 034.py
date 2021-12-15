N, K = map(int, input().split())
A = list(map(int, input().split()))

num_types = 1
num_dic = {A[0]: 1}
ans = 1
head = 0
tail = 1

while tail < N:
    if num_types > K:
        num_dic[A[head]] -= 1
        if num_dic[A[head]] == 0:
            num_types -= 1
        head += 1
    else:
        ans = max(ans, tail-head)
        tail += 1
        if A[tail-1] in num_dic:
            if num_dic[A[tail-1]] != 0:
                num_dic[A[tail-1]] += 1
            else:
                num_dic[A[tail-1]] = 1
                num_types += 1
        else:
            num_dic[A[tail-1]] = 1
            num_types += 1

if num_types <= K:
    ans = max(ans, tail-head)

print(ans)
