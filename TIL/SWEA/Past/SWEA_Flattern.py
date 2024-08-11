for testCase in range(1, 11):
    dump = int(input())

    reqList = list(map(int, input().split()))

    def bubbleSort(reqList, n):
        for i in range(n-1):
            for j in range(n-1-i):
                if reqList[j] > reqList[j+1]:
                    temp = reqList[j]
                    reqList[j] = reqList[j+1]
                    reqList[j+1] = temp
        return reqList
    for i in range(dump):
        reqList = bubbleSort(reqList, 100)
        reqList[0] += 1
        reqList[99] -= 1
        
    reqList = bubbleSort(reqList, 100)
    print(f'#{testCase} {reqList[99] - reqList[0]}')
    