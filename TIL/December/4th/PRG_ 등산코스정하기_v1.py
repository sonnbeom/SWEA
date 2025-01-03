from collections import deque


def get_distance(graph, start, n, summits, intensity, gates):
    summits = set(summits)
    gates = set(gates)
    temp_intensity = int(1e9)
    response = []
    q = deque()
    q.append((start, 0))  # 시작 노드, intensity
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    while q:
        node, cost = q.popleft()
        if cost > temp_intensity or cost > intensity:  # 비용이 인텐시티보다 비쌈
            continue

        for next_cost, next_node in graph[node]:
            if next_cost > intensity or next_cost > temp_intensity:
                continue
            elif visited[next_node]:
                continue
            elif next_node in gates:
                continue
            elif next_node in summits:
                cost = max(next_cost, cost)
                response.append((cost, next_node))
                temp_intensity = min(temp_intensity, cost)
            else:
                visited[next_node] = True
                cost = max(next_cost, cost)
                q.append((next_node, cost))
    return response


def solution(n, paths, gates, summits):
    intensity = int(1e9)  # 한 번 거리
    num = n
    graph = [[] for _ in range(n + 1)]

    for a, b, c in paths:
        graph[a].append((c, b))
        graph[b].append((c, a))
    for i in range(len(graph)):
        graph[i].sort()
    for g in gates:
        res = get_distance(graph, g, n, summits, intensity, gates)
        if res:
            res.sort()
            for r in res:
                d = r[0]
                node = r[1]
                if d > intensity:
                    break
                elif d < intensity:
                    intensity = min(d, intensity)
                    num = node
                elif d == intensity:
                    num = min(node, num)

    return [num, intensity]