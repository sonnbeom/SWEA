t = int(input())
for testCase in range(1, t+1):
    routes = []
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        routes.append((a, b))
        

    pCount = int(input())

    res = []
    for i in range(pCount):
        busStop = int(input())
        tempCount = 0
        for route in routes:
            left = route[0]
            right = route[1]
            if left <= busStop <= right:
                tempCount += 1
        res.append(tempCount)
        
    print(f'#{testCase}', *res)