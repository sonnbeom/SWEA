'''
가로를 체크하는 법 
왼쪽이 1인지 체크 -> 1이라면 실행x 길이측정이 불가임
세로 위가 1인지 체크 -> 1이라면 실행x 길이측정이 불가임

k 번 for문을 돕니다
가로면 우측이겠죠?  한칸씩 가서 길이를 더합니다 주어진 k값과 일치하면 res+1
00 01 02 

세로면 아래겠죠? 길이를 더합니다(범위 체크는 당연히) 주어진 k값과 일치하면  res+1
00 01
10
20

'''
# 01 일때 04 N-x값을 인자로 줘야 함 01 04 면 3을 주겠죠 01 02 03
# x = 1 n = 4     1 2 3 4 
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
print(ans)