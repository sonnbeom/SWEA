t = int(input())
for testCase in range(1, t+1):
    str1 = input()
    str2 = input()
    str3 = input()
    str4 = input()
    str5 = input()
    strList = [str1, str2, str3, str4, str5]
    maxLen = 0
    for str in strList:
        if len(str) > maxLen:
            maxLen = len(str)
    res = ''
    for idx in range(maxLen):
        if len(str1) > idx:
            res += str1[idx]
        if len(str2) > idx:
            res += str2[idx]
        if len(str3) > idx:
            res += str3[idx]
        if len(str4) > idx:
            res += str4[idx]
        if len(str5) > idx:
            res += str5[idx]
    print(f'#{testCase} {res}')