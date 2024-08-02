
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
# print(*raz)
# print(*iron)
res = 0
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
    print(f'lRange = {lRange} rRange = {rRange} tempCount = {tempCount}')
print(res)
        