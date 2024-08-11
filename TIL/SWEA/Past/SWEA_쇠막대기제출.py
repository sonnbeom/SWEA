t = int(input())
for testCase in range(1, t+1):
    
    arr = input()
    arrLen = len(arr)
    raz = []
    iron = []

    def getPartnerIdx(reqIdx):
        tempCount = 0
        for i in range(reqIdx, arrLen):
            if arr[i] == '(':
                tempCount += 1
            elif arr[i] == ')':
                tempCount -= 1
                if tempCount == 0:
                    return i
                
    for i in range(arrLen-1):
        if arr[i] == '(':
            if arr[i+1] == ')':
                raz.append((i, i+1))
            else:
                partIdx = getPartnerIdx(i)
                iron.append((i, partIdx))
    res = 0
    raz.sort()
    iron.sort()
    for ior in iron:
        tempCount = 1
        lRange = ior[0]
        rRange = ior[1]
        for ra in raz:
            left = ra[0]
            right = ra[1]
            if left > lRange and right < rRange:
                tempCount += 1
        res += tempCount
    print(f'#{testCase} {res}')
        