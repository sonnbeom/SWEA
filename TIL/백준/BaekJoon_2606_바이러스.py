from collections import deque

node = int(input())
edge = int(input())

arr = [[] for i in range(node+1)]
visited = [0] * (node+1)

for i in range(edge):
    a,b = map(int, input().split())
    arr[a] += [b]
    arr[b] += [a]

visited[1] = 1

q = deque([1])
while q:
    temp = q.popleft()
    for num in arr[temp]:
        if visited[num] == 0:
            q.append(num)
            visited[num] = 1

print(sum(visited)-1)
