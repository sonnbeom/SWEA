from collections import deque

node = int(input())
edge = int(input())

arr = [[] for _ in range(node+1)]
visited = [0] * (node+1)

for i in range(edge):
    a,b = map(int, input().split())
    arr[a] += [b]
    arr[b] += [a]

q = deque()
deque.append(1)
visited[1] = 1

while q:
    temp = q.popleft()
    for i in arr[temp]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
print(sum(visited)-1)