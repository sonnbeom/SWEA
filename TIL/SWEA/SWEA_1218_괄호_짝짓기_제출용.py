for testCase in range(1, 11):
    t = int(input())
    arr = list(input())
    visited = [False for _ in range(t)]

    def getPartner(req):
        if req == "{":
            return "}"
        elif req == "[":
            return "]"
        elif req == "(":
            return ")"
        elif req == "<":
            return ">"

    def checkVisited(idx):
        temp = arr[idx]
        partner = getPartner(temp)
        for i in range(idx + 1, t):
            if arr[i] == partner and visited[i] == False:
                visited[idx] = True
                visited[i] = True
                return
        
    for i in range(t):
        if visited[i] == False:
            checkVisited(i)

    if False in visited:
        print(f'#{testCase} 0')
    else:
        print(f'#{testCase} 1')