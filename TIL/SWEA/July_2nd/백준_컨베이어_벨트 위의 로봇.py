from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False for _ in range(n)])
ans = 0


while True:
    ans += 1
    belt.rotate(1)
    robot.rotate(1)

    robot[n-1] = False

    for i in range(n-2, -1, -1):
        if belt[i+1] > 0 and robot[i] == True and robot[i+1] == False:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[n-1] = False

    if belt[0] > 0:
        belt[0] -= 1
        robot[0] = True
    if belt.count(0) >= k:
        break

print(ans)