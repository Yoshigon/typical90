import heapq

N, M = map(int, input().split())
road = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a-1].append([c, b-1])
    road[b-1].append([c, a-1])


def dijkstra(start: int):
    distance = [-1] * N
    que = [(0, start)]
    heapq.heapify(que)
    while que:
        now = heapq.heappop(que)
        if distance[now[1]] != -1:
            continue
        distance[now[1]] = now[0]
        for town in road[now[1]]:
            if distance[town[1]] == -1:
                heapq.heappush(que, (now[0]+town[0], town[1]))
    return distance


dis_from_start = dijkstra(0)
dis_from_end = dijkstra(N-1)

for i in range(N):
    print(dis_from_start[i]+dis_from_end[i])
