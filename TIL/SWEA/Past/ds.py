from collections import deque

def bfs(startY, startX):
    q = deque([(startY, startX)])
    visited[startY][startX] = True
    
    while q:
        tempY, tempX = q.popleft()  # 큐의 앞에서 요소를 꺼냅니다.
        
        if arr[tempY][tempX] == 3:
            return 1
        
        for i in range(4):
            nowX = tempX + dx[i]
            nowY = tempY + dy[i]
            
            if 0 <= nowX < 100 and 0 <= nowY < 100 and not visited[nowY][nowX] and arr[nowY][nowX] == 0:
                visited[nowY][nowX] = True
                q.append((nowY, nowX))
                
    return 0

for t in range(10):  # 여러 테스트 케이스 처리
    input()  # 문제에서 요구하는 입력 무시
    arr = [list(map(int, input().strip())) for _ in range(100)]  # 100줄의 미로 입력 받기
    
    visited = [[False] * 100 for _ in range(100)]
    
    startX, startY = -1, -1
    for i in range(100):
        if 2 in arr[i]:
            startX = arr[i].index(2)
            startY = i
            break

    ans = bfs(startY, startX)
    print(f"#{t+1} {ans}")
