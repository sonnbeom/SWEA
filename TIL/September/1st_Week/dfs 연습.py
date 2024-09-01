'''
아웃풋
[1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 1, 2] [3, 2, 1]
'''

ex = [1, 2, 3]
n = 3
tempList = []
visited = [False for _ in range(n)]

def dfs(depth, arr):
    if depth == n:
        tempList.append(arr.copy())  # arr의 복사본을 추가
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(ex[i])
            dfs(depth + 1, arr)
            arr.pop()  # 마지막에 추가한 요소를 제거
            visited[i] = False  # 방문 기록을 되돌림

# dfs 호출
dfs(0, [])
print(*tempList)