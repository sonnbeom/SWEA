from collections import deque

def topology_sort():
    result = [0 for _ in range(node_cnt+1)]

    q = deque()

    for i in range(1, node_cnt):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += cost[now]

        for next_node in graph[now]:
            indegree[next_node] -= 1
            result[next_node] = max(result[now], result[next_node])
            if indegree[next_node] == 0:
                q.append(next_node)

    return result

node_cnt = int(input())

graph = [[] for _ in range(node_cnt+1)]
indegree = [0 for _ in range(node_cnt+1)]
cost = [0 for _ in range(node_cnt+1)]

for i in range(1, node_cnt+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    data = data[1:-1]
    for d in data:
        indegree[i] += 1
        graph[d].append(i)



ans = topology_sort()

print(ans)