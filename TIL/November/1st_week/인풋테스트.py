arr = [list(map(int, input().split())) for _ in  range(2)]
print(arr)

b = arr[:]
print(b)
b[0][0] = 100
print(b)