N = int(input())
user_names = {}
for i in range(N):
    tmp = input()
    if tmp not in user_names:
        user_names[tmp] = 1
        print(i+1)
