for _ in range(10):
    testCase = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False for _ in range(100)] for _ in range(100)]
    y = 99
    x = 0
    
    for i in range(100):
        if arr[99][i] == 2:
            x = i
            
    while y >= 0:
        
        # 좌로 가는 거임
        if x > 0  and arr[y][x-1] == 1 and visited[y][x-1] == False:
            while x > 0 and arr[y][x-1] == 1:
                x -= 1
                visited[y][x] = True
         # 우로 이동
        elif x < 99 and arr[y][x+1] == 1 and visited[y][x+1] == False:
            while x < 99 and arr[y][x+1] == 1:
                x += 1
                visited[y][x] = True
            # 위로 이동
        else:
            y -= 1
            visited[y][x] = True
            
    print(f'#{testCase} {x}')