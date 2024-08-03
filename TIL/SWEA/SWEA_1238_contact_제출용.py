for testCase in range(1, 11):
    t, start  = map(int, input().split())

    arr = [[0 for _ in range(101)] for _ in range(101)]
    visited = [False for _ in range(101)]

    tempList = list(map(int, input().split()))

    i = 0
    while i < t-1:
        a = tempList[i]
        b = tempList[i+1]

        arr[a][b] = b
        i += 2

    depthList = []

    def dfs(depth, start):
        visited[start] = True
        depthList.append((depth, start))
        for i in range(1, 101):
            if arr[start][i] != 0 and visited[i] == False:
                dfs(depth+1, i)
        
    dfs(1, start)
    depthList.sort()

    temp = 0
    listLen = len(depthList)
    depthMax = depthList[listLen-1][0]
    for depth, node in depthList:
        if depth == depthMax:
            if node > temp:
                temp = node
    print(f'#{testCase} {temp}')
