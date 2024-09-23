from collections import deque

def topology_sort():
    result = []
    q = deque()
    for i in range(1, node_cnt+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for idx in graph[now]:
            indegree[idx] -= 1
            if indegree[idx] == 0:
                q.append(idx)
    return result

node_cnt, edge = map(int, input().split())

indegree = [0 for _ in range(node_cnt+1)]
graph = [[] for _ in range(node_cnt+1)]
for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

res = topology_sort()
print(*res)