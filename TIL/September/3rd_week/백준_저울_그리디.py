n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr_sum = sum(arr)
tmp = [0, arr[0]]
ans = 0

for i in range(1, n):
    node = arr[i]
    start, end = tmp[0], tmp[1]
    node_start, node_end = start + node, end + node

    if node_start <= end+1:
        tmp[1] = node_end
    else:
        ans = end + 1
        break
if arr[0] != 1:
    print(1)
elif ans == 0:
    print(arr_sum+1)
else:
    print(ans)