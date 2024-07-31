t = int(input())

for testCase in range(1, t+1):
    def canWordGaro(arr, k , y, x, n):
        res = 0
        # x 부터 n-x 예를 들어 1부터 5까지 1 2 3 4 근데 전 1씩 더해야해요 바깥에 0을 두고 반복문 하면서 더하자
        # x = 1 n = 5  1 2 3 4  0 1 2 3 
        for i in range(k):
            nowX = x + i
            if nowX < n and arr[y][nowX] == 1:
                res += 1
        if x+k < n and arr[y][x+k] == 1:
            res = 0
        return res

    def canWordSero(arr, k, y, x, n):
        res = 0
        for i in range(k):
            nowY = y + i
            if nowY < n and arr[nowY][x] == 1:
                res += 1
        if y+k < n and arr[y+k][x] == 1:
            res = 0
        return res

    def isCorrect(req, con):
        if req == con:
            return True
        else: 
            return False
            
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for y in range(n):
        for x in range(n):
            if arr[y][x-1] != 1 or x == 0 and arr[y][x] == 1:
                res = canWordGaro(arr, k, y, x, n)
                if isCorrect(res, k):
                    ans += 1
            if arr[y-1][x] != 1 or y== 0 and arr[y][x] == 1:
                res = canWordSero(arr, k, y, x, n)
                if isCorrect(res, k):
                    ans += 1
                    
    print(f'#{testCase} {ans}')