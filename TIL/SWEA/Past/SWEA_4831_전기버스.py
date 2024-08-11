from collections import deque

k, n, m = map(int, input().split())
arr = [0 for _ in range(n+1)]
bus = list(map(int, input().split()))

for index in bus:
    arr[index] = 1
temp = 0

def getMaxIdx(temp):
    maxIdxList = []
    for idx in range(temp+1, temp+k+1):
        if arr[idx] == 1:
            maxIdxList.append(idx)
    if len(maxIdxList) == 0:
        return 0
    else:
        maxIdxList.sort(reverse=True)
        return maxIdxList[0]
    
q = deque([0])

res = 0
while q:
    temp = q.pop()
    if temp + k >= n:
        break
    idx = getMaxIdx(temp)
    if idx == 0:
        break
    q.append(idx)
    res += 1
        
print(res)