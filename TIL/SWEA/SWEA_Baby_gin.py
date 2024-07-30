def isSame(reqList, n):
    res = -1
    for i in range(n-2):
        tempCount = 1
        for j in range(i+1, n-i):
            if reqList[i] == reqList[j]:
                tempCount += 1
                if tempCount == 3:
                    res = reqList[i]
    return res

def bubbleSort(reqList, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if reqList[j] > reqList[j+1]:
                temp = reqList[j]
                reqList[j] = reqList[j+1]
                reqList[j+1] = temp
    return reqList

def isSeq(reqList, n):
    tempList = []
    temp = -1
    res = []
    for i in range(n-2):
        temp = reqList[i]
        tempList.append(temp)
        for j in range(i+1, n):
            if temp +1 == reqList[j]:
                temp += 1
                tempList.append(temp)
                if len(tempList) == 3:
                    for i in range(3):
                        res.append(tempList[i])
    return res
                

arr = list(map(int, input()))
res = 0
# 같은 숫자인지 체크
resIsSame = isSame(arr, 6)
#같은 숫자임
if resIsSame != -1:
    for i in range(3):
        arr.remove(resIsSame)
    resIsSameTwice = isSame(arr, 3)
    if resIsSameTwice != -1:
        res = 1
    else:
        sortedList = bubbleSort(arr, 3)
        #같은 갯수가 3개면 순서대로인지 확인
        resIsSeq = isSeq(sortedList, 3)
        if len(resIsSeq) == 3:
            res = 1
        elif len(resIsSeq) != 3:
            fianlResisSame = isSame(sortedList, 3)
            if fianlResisSame != -1:
                res = 1
else:
    sortedList = bubbleSort(arr, 6)
    resIsSeq = isSeq(sortedList, 6)
    if len(resIsSeq) == 3:
        for i in range(3):
            sortedList.remove(resIsSeq[i])
        twiceSortedList = bubbleSort(sortedList, 3)
        resTwiceIsSeq = isSeq(twiceSortedList, 3)
        if len(resTwiceIsSeq) == 3:
            res =1
print(res)





# def isSeq(reqList):
#     for i in range(2):
#         if reqList[i] + 1 == reqList[i+1]:
#             continue
#         else:
#             return False
#     return True
# def isSeqTwice(reqList):
#     for i in range(3,5):
#         if reqList[i] + 1 == reqList[i+1]:
#             continue
#         else:
#             return False
#     return True