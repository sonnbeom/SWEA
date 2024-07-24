import sys

input = sys.stdin.readline
n = int(input())
temp = []
dic = {}
_sum = 0
for i in range(n):
    x = int(input())
    temp.append(x)
    _sum += x
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

temp.sort()

print(round(_sum/n))

print(temp[n//2])

numbers = []
freq = max(dic.values())
for key, value in dic.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])


print(temp[n-1] - temp[0])

