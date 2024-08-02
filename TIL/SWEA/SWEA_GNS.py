testCase, t = input().split()
n = int(t)

dic = {"ZRO" : [],  "ONE" : [],"TWO" : [],"THR" : [],"FOR" : [],"FIV" : [],"SIX" : [],"SVN" : [],"EGT" : [],"NIN" : []}
req = list(input().split())

for numStr in req:
    if numStr == "ZRO":
        dic["ZRO"].append("ZRO ")
    elif numStr == "One":
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
for key, values in dic.items():
    print(*values, end = '')
print