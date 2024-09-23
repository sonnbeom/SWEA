

n = int(input())
arr = list(map(int, input().split()))

ans = [-1 for _ in range(n)]

stack = []

stack.append(0)

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)