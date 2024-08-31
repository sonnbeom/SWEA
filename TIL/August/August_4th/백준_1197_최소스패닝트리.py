def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int,input().split())
parent = [0 for _ in range(V+1)]

for i in range(V+1):
    parent[i] = i

edges = []
total_cost = 0
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(E):
    cost, a, b = edges[i]
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent != b_parent:
        union(parent, a, b)
        total_cost += cost

print(total_cost)