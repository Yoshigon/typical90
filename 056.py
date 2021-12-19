N, S = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (S+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S):
        a, b = goods[i]
        if dp[i][j] != -1:
            if j+a <= S:
                dp[i+1][j+a] = 1
            if j+b <= S:
                dp[i+1][j+b] = 1

if dp[-1][-1] == 1:
    ans = ''
    total = S
    for i in range(N, 0, -1):  # i日目に買ったものを考える
        if total - goods[i-1][0] >= 0:
            if dp[i-1][total-goods[i-1][0]] == 1:
                total -= goods[i-1][0]
                ans = 'A' + ans
            else:
                total -= goods[i-1][1]
                ans = 'B' + ans
        else:
            total -= goods[i-1][1]
            ans = 'B' + ans
    print(ans)

else:
    print("Impossible")

# 別解
# N, S = map(int, input().split())
# former = {0: ''}
# latter = {0: ''}
#
# for _ in range(N//2):
#     A, B = map(int, input().split())
#     next_former = {}
#     for key in former:
#         if key >= S:
#             continue
#         way = former[key] + 'A'
#         next_former[key+A] = way
#         way = former[key] + 'B'
#         next_former[key+B] = way
#     former = next_former
#
# for _ in range(N//2, N):
#     A, B = map(int, input().split())
#     next_latter = {}
#     for key in latter:
#         if key >= S:
#             continue
#         way = latter[key] + 'A'
#         next_latter[key + A] = way
#         way = latter[key] + 'B'
#         next_latter[key + B] = way
#     latter = next_latter
#
#
# for key in former:
#     if S-key in latter:
#         print(former[key] + latter[S-key])
#         exit()
# print("Impossible")
