n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
res = 0
for i in range(n):
    temp = arr[i] - (i + 1 - 1)
    if temp < 0:
        break
    res += temp
print(res)