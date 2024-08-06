t = 10
for testCase in range(1, t+1):
    def bfs(start):
        queue = [start]
        visited[start] = 0

        while queue:
            temp = queue.pop(0)
            for i in arr[temp]:
                if visited[i] == 0:
                    visited[i] = visited[temp] + 1
                    queue.append(i)

    t, start  = map(int, input().split())

    arr = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]

    tempList = list(map(int, input().split()))

    for i in range(0, t, 2):
        arr[tempList[i]].append(tempList[i+1])

    bfs(start)

    maxDepth = max(visited)

    ans = 0 
    for i in range(len(arr)):
        if visited[i] == maxDepth and i > ans:
            ans = i
    print(f'#{testCase} {ans}')