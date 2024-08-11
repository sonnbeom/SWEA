k = int(input())
for _ in range(k):
    testCase, t = input().split()
    n = int(t)

    dic = {"ZRO" : [],  "ONE" : [],"TWO" : [],"THR" : [],"FOR" : [],"FIV" : [],"SIX" : [],"SVN" : [],"EGT" : [],"NIN" : []}
    req = list(input().split())
    keyList = ["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
    for numStr in req:
        if numStr == "ZRO":
            dic["ZRO"].append("ZRO ")
        elif numStr == "ONE":
            dic["ONE"].append("ONE ")
        elif numStr == "TWO":
            dic["TWO"].append("TWO ")
        elif numStr == "THR":
            dic["THR"].append("THR ")
        elif numStr == "FOR":
            dic["FOR"].append("FOR ")
        elif numStr == "FIV":
            dic["FIV"].append("FIV ")
        elif numStr == "SIX":
            dic["SIX"].append("SIX ")
        elif numStr == "SVN":
            dic["SVN"].append("SVN ")
        elif numStr == "EGT":
            dic["EGT"].append("EGT ")
        elif numStr == "NIN":
            dic["NIN"].append("NIN ")
            
    print(testCase)
    for idx in range(10):
        key = keyList[idx]
        print(*dic[key], end='')
    print()