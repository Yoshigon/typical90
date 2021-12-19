N, S = map(int, input().split())
former = {0: ''}
latter = {0: ''}

for _ in range(N//2):
    A, B = map(int, input().split())
    next_former = {}
    for key in former:
        if key >= S:
            continue
        way = former[key] + 'A'
        next_former[key+A] = way
        way = former[key] + 'B'
        next_former[key+B] = way
    former = next_former

for _ in range(N//2, N):
    A, B = map(int, input().split())
    next_latter = {}
    for key in latter:
        if key >= S:
            continue
        way = latter[key] + 'A'
        next_latter[key + A] = way
        way = latter[key] + 'B'
        next_latter[key + B] = way
    latter = next_latter


for key in former:
    if S-key in latter:
        print(former[key] + latter[S-key])
        exit()
print("Impossible")
