from collections import deque



n, k = map(int, input().split())
r = list(map(int, input().split()))
belt = deque(r)

print(f'belt = {belt}')
robots = [] # idx를 넣자
# 회전 => 로봇도 회전 idx += 1을 해주자 만약 2n을 넘어간다면 첫번째 자리로
# 첫번째 로봇부터 이동 (2n을 넘어가는지 체크)
# 올리는 위치에 있는 칸의 내구도가 0이 아니고 로봇이 없다면 올린다.
# 내구도가 0인 칸의 개수를 측정하여 k개 이상이면 break
cnt = 0
while True:
    cnt += 1

    print(f'초기 값 cnt = {cnt} belt = {belt} robots = {robots}')
    belt.rotate(1) # 벨트 회전
    temp_robot = []

    print(f'회전 후cnt = {cnt} belt = {belt} robots = {robots} temp_robot = {temp_robot} ')
    for robot_idx in robots:
        idx = (robot_idx + 1) % (2*n)
        if idx == n-1:
            continue
        next_idx = (robot_idx + 2) % (2*n)
        if next_idx == n-1:
            if belt[next_idx] > 0:
                belt[next_idx] -= 1
            continue
        elif belt[next_idx] < 1:
            temp_robot.append(robot_idx)
            continue
        elif next_idx in temp_robot:
            temp_robot.append(robot_idx)
            continue
        belt[next_idx] -= 1
        temp_robot.append(next_idx)

    print(f'로봇 이동 후cnt = {cnt} belt = {belt} robots = {robots} temp_robot = {temp_robot}')
    if belt[0] > 0 and 0 not in temp_robot:
        temp_robot.append(0)
        belt[0] -= 1
    print(f'로봇 놓은 후cnt = {cnt} belt = {belt} robots = {robots} temp_robot = {temp_robot}')
    zero = 0
    for b in belt:
        if b == 0:
            zero += 1
    if zero >= k:
        break
    robots = temp_robot

print(f'cnt = {cnt}')



