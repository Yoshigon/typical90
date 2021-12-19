from collections import deque
Q = int(input())
deck = deque([])
count = 0
output_idx = []

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        deck.appendleft(x)
        count += 1
    elif t == 2:
        deck.append(x)
    elif t == 3:
        x -= count
        output_idx.append(x)

deck = list(deck)
for idx in output_idx:
    print(deck[idx+count-1])
