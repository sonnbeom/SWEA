from collections import deque


def func(info, graph, start, sheep_cnt):
    q = deque()
    q.append((start, sheep_cnt[start][0], sheep_cnt[start][1]))  # 현재 노드, 양 숫자, 늑대 숫자, 차이
    while q:
        node, sheep, wolf = q.popleft()
        print(f'node ={node} sheep ={sheep} wolf = {wolf}')
        if sheep_cnt[node][0] - sheep_cnt[node][1] > sheep - wolf:
            continue
        for next_node in graph[node]:
            animal = info[next_node]
            if animal == 0:
                sheep += 1
            else:
                wolf += 1
            new_diff = sheep - wolf
            o_next_node = sheep_cnt[next_node][0] - sheep_cnt[next_node][1]
            if o_next_node < new_diff:
                sheep_cnt[next_node][0] = sheep
                sheep_cnt[next_node][1] = wolf
                q.append((next_node, sheep, wolf))
    print(sheep_cnt)
    return sheep_cnt


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
    sheep_dis = [[int(1e9), int(1e9)] for _ in range(len(info))]
    sheep_dis[0][0] = 1
    sheep_dis[0][1] = 0
    sheep_cnt = func(info, graph, 0, sheep_dis)
    next_node = []
    for i in range(1, len(sheep_cnt)):
        temp = sheep_cnt[i]
        if temp[0] - temp[1] > 0:
            next_node.append(i)
    for node in next_node:
        sheep_cnt = func(info, graph, node, sheep_cnt)
    print(f'sheep_cnt = {sheep_cnt}')








