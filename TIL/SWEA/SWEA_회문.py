reqStr = input()
reqLen = len(reqStr)

divNum = reqLen // 2
res = 1
for i in range(divNum):
    if reqStr[i] != reqStr[reqLen-1]:
        res += 1
    reqLen -= 1
if res == 1:
    print(res)
else:
    print(0)