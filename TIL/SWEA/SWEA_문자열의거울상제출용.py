t = int(input())
for testCase in range(1, t+1):
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
    print(f'#{testCase} {resStr}')