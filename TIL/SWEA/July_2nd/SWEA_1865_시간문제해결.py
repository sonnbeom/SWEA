n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
ans = -1

def r(result, depth):
    global ans
    if depth == n:
        if ans < result:
            ans = result
        return
    if result <= ans:
        return
    for i in range(n):
        if visited[i] == False:
            newResult = result * arr[depth][i] * 0.01
            visited[i] = True
            r(newResult, depth + 1)
            visited[i] = False
r(1, 0)
ans *= 100
print(f"{ans:6f}")

