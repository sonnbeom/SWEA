'''
뒤집고 반대 리턴 해서 비어있는 스트링에 더한다.
'''
def getReverseChar(req):
    if req == "b":
        return "d"
    elif req == "d":
        return "b"
    elif req == "p":
        return "q"
    else:
        return "p"

reqStr = input()
lastIdx = len(reqStr)
reverseStr = ''
for i in range(lastIdx):
    temp = reqStr[lastIdx-1]
    reverseStr += temp
    lastIdx -= 1

resStr = ''
for i in range(len(reverseStr)):
    tempChar = getReverseChar(reverseStr[i])
    resStr += tempChar
print(resStr)