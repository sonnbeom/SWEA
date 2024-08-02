small = input()
big = input()

dic = {}
duplicationList = []
for strSmall in small:
    if strSmall not in duplicationList:
        dicValue = 1
        for strBig in big:
            if strSmall == strBig:
                if dic.get(strSmall):
                    dicValue += 1
                    dic.get(strSmall).append(dicValue)
                else:
                    dic[strSmall] = [dicValue]
        duplicationList.append(strSmall)
res = 0
for key, value in dic.items():
    tempList = dic.get(key)
    if tempList[-1] > res:
        res = tempList[-1]
print(res)