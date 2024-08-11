'''
좌 우 없으면 아래로 좌로 가면 좌좌좌  우로 가면 우우우 아래는 하나만
y += 1 부분에 else를 적었다. 이걸로 5시간 날렸다... 왜 while문에 갇힐까?
일단 우리가 원하는 동작에 대해 기술해보자. 
1. 좌, 우로 갈 길이 있으면 그 방향으로 쭉 간다.
2. 갈 길이 없으면 아래로 한칸 내려가기
3. 1,2를 반복한다.

1,2번을 읽어보면 한 방향으로 쭉 가다가 막히면 아래 방향으로 한칸을 내려가는 게 무조건 성립되어야 한다.
만약 아래 방향으로 내려가지 않는다면
좌로 끝까지 이동 우로 끝까지 이동 이 과정을 무한반복하게 된다.

이걸 코드로 풀어설명하자면 else라는 조건문을 걸게 되면 좌로 이동 우로 이동... 이러한 과정이 무한반복된다.
만약 내가 원하는 방식으로 하고 싶었다면
visited 배열을 만들어서 방문했다면 True 방문하지 않은 상태는 False라면 좌->우->좌->우 이러한 무한반복에
걸릴 일이 없다.

이러한 방법은 단점이 없을까? 
메모리에 문제가 없다면 가능할 것이다. for문을 돌 때마다 100 * 100 배열을 만드는 리소스가 든다.
그런데 else 하나만 안 쓰면 충분히 가능하다.

'''
def countDistance(start):
    y = 0
    x = start
    count = 0
    while y != 99:
        if x - 1 >= 0 and arr[y][x-1] == 1:
            while x - 1 >= 0 and arr[y][x-1] == 1:
                count += 1
                x -= 1
        elif x + 1 <= 99 and arr[y][x+1] == 1:
            while x + 1 <= 99 and arr[y][x+1] == 1:
                count += 1
                x += 1
        y += 1
    return count


T = 10
for t in range(T):
    testCaseIndex = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    startList = []
    for i in range(100):
        if arr[0][i] == 1:
            startList.append(i)

    countList = []
    for idx in startList:
        countList.append(countDistance(idx))
    res = startList[countList.index(min(countList))]
    print(f'#{testCaseIndex} {res}')
