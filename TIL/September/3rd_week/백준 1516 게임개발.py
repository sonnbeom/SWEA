from collections import deque

def topology_sort():
    result = [0 for _ in range(n+1)]
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()

        result[now] += cost[now]
        for next_node in building[now]:
            indegree[next_node] -= 1
            result[next_node] = max(result[next_node], result[now])
            if indegree[next_node] == 0:
                q.append(next_node)
    return result

n = int(input())

building = [[] for _ in range(n+1)]

indegree = [0 for _ in range(n+1)]

cost = [0 for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    building_data = data[1:-1]

    for j in building_data:
        indegree[i] += 1
        building[j].append(i)

ans = topology_sort()
for i in range(1, n+1):
    print(ans[i])
