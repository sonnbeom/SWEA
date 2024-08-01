'''
버스 노선이 들어오면
list에 튜플 형태로 넣자

버정 위치가 들어오면
for문을 돈다.
list에 튜플에서 idx 0번과 1번 사이라면 temp += 1
resList에 담는다
출력 유노

'''
routes = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    routes.append((a, b))
    

pCount = int(input())

res = []
for i in range(pCount):
    busStop = int(input())
    tempCount = 0
    for route in routes:
        left = route[0]
        right = route[1]
        if left <= busStop <= right:
            tempCount += 1
    res.append(tempCount)
    
    
print(*res)