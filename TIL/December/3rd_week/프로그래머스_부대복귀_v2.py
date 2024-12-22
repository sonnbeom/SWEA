from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1 for _ in range(n + 1)]
    distance[destination] = 0

    q = deque()
    q.append(destination)

    while q:
        node = q.popleft()
        next_node_d = distance[node] + 1
        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = next_node_d
                q.append(next_node)
    for s in sources:
        answer.append(distance[s])

    return answer
