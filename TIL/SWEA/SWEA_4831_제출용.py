t = int(input())
for testCase in range(1, t+1):
    k, n, m = map(int, input().split())
    arr = [0 for _ in range(n+1)]
    bus = list(map(int, input().split()))

    for index in bus:
        arr[index] = 1
    temp = 0

    def bubbleSort(arr, n):
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] < arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr

    def getMaxIdx(temp):
        maxIdxList = []
        for idx in range(temp+1, temp+k+1):
            if arr[idx] == 1:
                maxIdxList.append(idx)
        if len(maxIdxList) == 0:
            return 0
        else:
            resList = bubbleSort(maxIdxList, len(maxIdxList))
            return resList[0]
        
    q = [0]

    res = 0
    while q:
        temp = q.pop()
        if temp + k >= n:
            break
        idx = getMaxIdx(temp)
        if idx == 0:
            res = 0
            break
        q.append(idx)
        res += 1
            
    print(f'#{testCase} {res}')