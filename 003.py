import heapq

N = int(input())
roads = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    roads[a-1].append(b-1)
    roads[b-1].append(a-1)


def dijkstra(start: int):
    que = [(0, start)]
    visited = {start: 1}
    heapq.heapify(que)
    dist = 0
    now = start
    while que:
        dist, now = heapq.heappop(que)
        for town in roads[now]:
            if town not in visited:
                visited[town] = 1
                heapq.heappush(que, (dist+1, town))
    return dist, now


distance, furthest = dijkstra(0)
distance, furthest = dijkstra(furthest)

print(distance+1)
