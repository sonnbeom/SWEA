import sys
sys.setrecursionlimit(10**5)


def dfs(depth, tmp_sum):
    check[tmp_sum] = True
    print(f'tmp_sum = {tmp_sum}')
    if depth == n:
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, tmp_sum+arr[i])
            visited[i] = False


n = int(input())
arr = list(map(int, input().split()))

arr.sort()

tmp_set = set()
arr_sum = sum(arr)
check = [False for _ in range(arr_sum+1)]
visited = [False for _ in range(n+1)]
check[0] = True

dfs(0, 0)

ans = 0
for i in range(arr_sum):
    if not check[i]:
        ans = i
        break
print(ans)
