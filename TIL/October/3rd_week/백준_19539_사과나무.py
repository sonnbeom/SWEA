n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = arr[i] % 3

res = True
while True:
    two_cnt = 1
    one_cnt = 1
    print(arr)
    for i in range(n):
        if arr[i] == 2:
            arr[i] = 0
            two_cnt = 0
            break
    for i in range(n):
        if arr[i] == 1:
            arr[i] = 0
            one_cnt = 0
            break
    print(f'two_cnt = {two_cnt} one_cnt = {one_cnt}')
    if two_cnt == 1 or one_cnt == 1:
        res = False
        break


# print(arr)
# for i in range(n):
#     if arr[i] != 0:
#         res = False
#         break
if res:
    print("YES")
else:
    print("NO")