'''
행 세로 y
열 가로 x 

1. 크기가 작은 순서대로 출력
2. 크기가 같다면 행이 작은 순서대로 출력

dic key : 크기 value: 행
같을 수가 없는 것은 무엇일까? 없음
크기는 같을 수 있음 행끼리도 같을 수 있음 열끼리도

연결 시켜보자.

크기

딕셔너리 안에 딕셔너리 어떤데

dicParent key: 크기 value : 행 12  3 4 4 3
dicChild key:행 value: 열 4 3, 3 4
list에 담아 행을  정렬 오름차순
그래서 tempList[i] dicChild[tempList[i]] 출력

if: .items() 돌아서 해당 key 가진 딕셔너리 크기가 1 이상이다?
해당 리스트 for문을 돌며 key, value을 리턴하면 된다.
elif: items() 돌아서 해당 key 가진 딕셔너리 크기가 1이다
 key, value을 리턴하면 된다.
'''
'''
00 01 좌 우 상 하
10 11
'''

def checkVisited(x, nowX, nowY):
    for i in range(x, nowX + 1):
        visited[nowY][i] = True

def getSize(y, x):
    visited[y][x] = True 
    nowX = x
    nowY = y
    while 0 <= nowX +1 < n:
        if arr[y][nowX+1] != 0 and visited[y][nowX+1] == False:
            nowX += 1
            visited[y][nowX] = True
        else:
            break
    while 0 <= nowY +1 < n:
        if arr[nowY+1][x] != 0 and visited[nowY+1][x] == False:
            nowY += 1
            checkVisited(x, nowX, nowY)
        else:
            break
    garo = nowX - x + 1
    sero = nowY - y + 1
    return [garo * sero, sero, garo]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for i in range(n)] for _ in range(n)]

size = 0
parentList = [[] for _ in range((n+1)*(n+1))]

count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and visited[i][j] == False:
            res =getSize(i, j)
            listChild = [res[1], res[2]]
            parentList[res[0]].append(listChild)
            count += 1
print(f'#{count}', end= ' ')
for child_list in parentList:
    child_list.sort()
    for child in child_list:
        if child:
           print(child[0], child[1], end=' ')

'''
 1. 가로 다 갔다가
    처음 인덱스에서 다시 가로
1. 가로 가도 돼? 체크
2. 가로 가도 돼 체크 해서 가로 길이 리턴 받음 (방문하면 False로)
3. 세로 길이 가도 돼? 체크 +1
4. 가로 가도 돼 리턴 받음 (방문하면 False로)

리턴 튜플로 (2,4)

'''

'''
[
    [3,4]
    [2,6]
    [4,3]
]
행을 정렬한 리스트를 만듬
[2, 3, 4]
빈 배열 만든다.
for index, value in enurmate(arr):
    print(index, value)
arr[3] = 4
arr[2] = 6
arr[4] = 3
'''