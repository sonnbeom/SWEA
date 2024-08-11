def find_parent(parent ,x):
    if parent[x] != x:
        #  find_parent(parent, parent[x]) 경로압축...?
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())
for tc in range(1, t+1):
    node, edge = map(int, input().split())
    graph = []
    for i in range(edge):
        a, b, cost = map(int, input().split())
        graph.append([cost, a, b])
    graph.sort()

    parent = [0] * (node+1)
    for i in range(1, node+1):
        parent[i] = i
    costs = 0
    for i in range(edge):
        cost, a, b = graph[i]
        a_parent = find_parent(parent, a)
        b_parent = find_parent(parent ,b)
        if a_parent != b_parent:
            union_find(parent, a_parent, b_parent)
            costs += cost
    print(f'#{tc} {costs}')


