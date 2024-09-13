import heapq

def dijkstra(start):
    total_cost = [int(1e9) for _ in range(node_cnt+1)]
    total_cost[start] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        if total_cost[node] < cost:
            continue
        for next_node, plus_cost in graph[node]:
            if cost + plus_cost < total_cost[next_node]:
                total_cost[next_node] = cost + plus_cost
                prev_node[next_node] = node
                heapq.heappush(q, (cost+plus_cost, next_node))
    return total_cost



node_cnt = int(input())
edge = int(input())

graph = [[] for _ in range(node_cnt+1)]

for i in range(edge):
    start, goal, cost = map(int, input().split())
    graph[start].append([goal, cost])

start, target = map(int, input().split())
prev_node = [0 for _ in range(node_cnt+1)]
total_cost = dijkstra(start)
path = [target]
prev_one_node = target

while prev_one_node != start:
    prev_one_node = prev_node[prev_one_node]
    path.insert(0, prev_one_node)

print(total_cost[target])
print(len(path))
for n in path:
    print(n, end=' ')