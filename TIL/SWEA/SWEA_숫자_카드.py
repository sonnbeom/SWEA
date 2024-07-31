'''
1.
2. 길이가 100개인 리스트
3. input은 idx count +=1 
4. 예: 4 => arr[4] +=1 
5. for문을 돌며 가장 맥스 카운트를 가져온다.
6. 맥스 카운트에 해당하는 idx를 리스트에 담고 최대값을 산출한다.
'''

arr = [0 for _ in range(100)]
n = int(input())
req = input()

for i in req:
    temp = int(i)
    arr[temp] += 1

maxIndex = 0
for numCount in arr:
    if numCount > maxIndex:
        maxIndex = numCount

tempList = []
for idx in range(100):
    if arr[idx] == maxIndex:
        tempList.append(idx)
maxNum = 0
for num in tempList:
    if num > maxNum:
        maxNum = num
print(maxNum, maxIndex)