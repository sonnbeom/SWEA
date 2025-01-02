from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * (2 * n))  # 로봇의 위치를 저장 (True: 로봇 있음, False: 로봇 없음)

steps = 0
while True:
    steps += 1

    # 1. 벨트 회전
    belt.rotate(1)
    robots.rotate(1)
    robots[n - 1] = False  # n-1 위치의 로봇은 내려감

    # 2. 로봇 이동
    for i in range(n - 2, -1, -1):  # 로봇을 뒤에서부터 이동
        if robots[i] and not robots[i + 1] and belt[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            belt[i + 1] -= 1
    robots[n - 1] = False  # n-1 위치의 로봇은 내려감

    # 3. 로봇 올리기
    if belt[0] > 0 and not robots[0]:
        robots[0] = True
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수를 체크
    if belt.count(0) >= k:
        break

print(steps)
