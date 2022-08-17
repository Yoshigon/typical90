N = int(input())
ids = dict()

for i in range(N):
    s = input()
    if s not in ids:
        ids[s] = i+1

for v in sorted(ids.values()):
    print(v)
