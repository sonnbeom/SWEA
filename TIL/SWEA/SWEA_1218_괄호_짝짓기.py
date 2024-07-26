'''
181
(({<(({{[[[[<<[[(<[[{([{{{[<[[[{<<(<[[{}[]{}{}[]]]><<>{})[]{}><>[]<>><>}][]]<>{}]>]()}()()(){}}}{}][])(){}<>()}]{}[]]>()[][][]){}]]{}[]<>><>{}[]{}<>>]]]][]{}{}[]()}}))>}<>{}()))[][]

index에 반대에 있으면 되는 거 아닌가
1. for문을 돈다.
2. 예를 들어 (가 나온 경우 )가 나온 인덱스를 찾는다.
3. 거기서 for문을 돌면서 짝을 찾아준다.
4. for문을 돌고 짝을 찾고
5. 방문한 곳이라면 true로 체크한다.
6. visited를 쭉 돌고 false가 없는 경우 1을 리턴 있는 경우 0을 리턴
'''
t = int(input())

arr = list(input())
visited = [False for _ in range(t)]

def getPartner(req):
    if req == "{":
        return "}"
    elif req == "[":
        return "]"
    elif req == "(":
        return ")"
    elif req == "<":
        return ">"

def checkVisited(idx):
    temp = arr[idx]
    partner = getPartner(temp)
    for i in range(idx + 1, t):
        if arr[i] == partner:
            visited[idx] = True
            visited[i] = True
            return
    
    
for i in range(t):
    if visited[i] == False:
        checkVisited(i)
if False in visited:
    print(0)
else:
    print(1)