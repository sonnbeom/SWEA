
n = int(input())
triangle = []

for i in range(n):
    tri = [1]
    for j in range(i-1):
        parent = triangle[-1]
        if j < i:
            tmp = parent[j]
            tmp += parent[j+1]
            tri.append(tmp)
    tri.append(1)
    triangle.append(tri)

first = triangle[0]
first.pop(0)
for i in triangle:
    print(*i)
