from collections import deque


def get_animal(i, animal):
    if i == 0:
        return [animal[0] + 1, animal[1]]
    else:
        return [animal[0], animal[1] + 1]


def bfs(visited, cnt, graph, info):
    q = deque()
    q.append(0)  # 시작 노드
    visited[0] = True
    while q:
        if False not in visited:
            return cnt
        node = q.popleft()

        for next_node in graph[node]:

            animal = get_animal(info[next_node], cnt[node])
            next_sheep = animal[0]
            next_wolf = animal[1]
            if (next_sheep - next_wolf) > (cnt[next_node][0] - cnt[next_node][1]):
                # cnt[next_node][0] = next_sheep
                # cnt[next_node][1] = next_wolf
                print(f'now ={node} next_node = {next_node} cnt[next_node] ={cnt[next_node]} next_sheep={next_sheep} next_wolf ={next_wolf}')
                cnt[next_node][0] = max(next_sheep, cnt[next_node][0])
                cnt[next_node][1] = max(next_wolf, cnt[next_node][1])
            q.append(next_node)
            visited[next_node] = True


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for _ in range(len(info))]
    cnt = [[0, 0] for _ in range(len(info))]
    cnt[0][0] = 1
    cnt = bfs(visited, cnt, graph, info)
    print(f'cnt = {cnt}')
    for i in range(len(cnt)):
        print(f'i={i}번째 cnt = {cnt[i]}')

info = 	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
solution(info, edges)