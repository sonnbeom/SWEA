t = int(input())
for testCase in range(1, t+1):
    arr = [0 for _ in range(100)]
    n = int(input())
    req = input()

    for i in req:
        temp = int(i)
        arr[temp] += 1

    maxIndex = 0
    for numCount in arr:
        if numCount > maxIndex:
            maxIndex = numCount

    tempList = []
    for idx in range(100):
        if arr[idx] == maxIndex:
            tempList.append(idx)
    maxNum = 0
    for num in tempList:
        if num > maxNum:
            maxNum = num
    print(f'#{testCase} {maxNum} {maxIndex}')