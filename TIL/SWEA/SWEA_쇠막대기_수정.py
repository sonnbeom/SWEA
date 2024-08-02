arr = input()
arrLen = len(arr)

result = 0
cnt = 0

for i in range(arrLen):
    if arr[i] == '(':
        cnt += 1
    else:
        cnt -= 1
        if arr[i-1] == '(':
            result += cnt
        else:
            result += 1
print(result)