from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robo = [-1 for _ in range(2*n)]
robot = deque(robo)
ans = 0
zero = 0
w = 0
while k > zero:
    ans += 1
    belt.rotate(1)
    robot.rotate(1)
    for i in range(w-1, -1, -1):
        t = i+2 % (2*n)
        if robot[t] == -1 and belt[t] != 0: #로봇이 없고 벨트 값이 0이 아니라면
            robot[i] = -1
            robot[t] = t #로봇위치 1칸 이동
            belt[t] -= 1 # 벨트 값 감소
            if belt[t] == 0: # 벨트 값이 0이라면 ans 증가
                k -= 1
                zero += 1
                if k == zero:
                    break
            if robot[t] == n-1: # 만약 내리는 위치라면 없애
                robot[n-1] = -1
                w -= 1
                # robot.remove(robot[i])
    if belt[0] != 0 and robot[0] == -1:
        belt[0] -= 1
        w += 1
        if belt[0] == 0:
            k -= 1
            zero += 1
            if k == zero:
                break
        robot[0] = 0


print(ans)