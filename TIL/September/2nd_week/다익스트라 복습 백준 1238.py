import heapq

def dijkstra(start):
    total_time = [int(1e9) for _ in range(node_cnt+1)]
    total_time[start] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start)) # 시간, 다음 노드

    while q:
        time, node = heapq.heappop(q)

        if total_time[node] < time:
            continue
        for next_node, next_time in graph[node]:
            if next_time + time < total_time[next_node]:
                total_time[next_node] = next_time + time
                heapq.heappush(q, (next_time + time, next_node))
    return total_time

node_cnt, edge, X = map(int, input().split())

graph = [[] for _ in range(node_cnt+1)]

for _ in range(edge):
    start, goal, time = map(int, input().split())
    graph[start].append([goal, time])

time_list = dijkstra(X)
time_list[0] = 0

for i in range(1, node_cnt+1):
    if i != X:
        res = dijkstra(i)
        time_list[i] += res[X]

print(max(time_list))