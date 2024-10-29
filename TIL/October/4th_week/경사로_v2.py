def solution(req_num, req_bool):
    visited = [False for _ in range(n)]
    temp = []
    idx = 0

    # 가로/세로 줄 가져오기
    if req_bool:
        for i in range(n):
            temp.append(arr[i][req_num])
    else:
        for i in range(n):
            temp.append(arr[req_num][i])

    while idx < n - 1:
        # 현재 칸과 다음 칸의 높이가 같은 경우
        if temp[idx] == temp[idx + 1]:
            idx += 1
            continue

        # 높이 차이가 1보다 크면 경사로를 설치할 수 없음
        if abs(temp[idx] - temp[idx + 1]) > 1:
            return False

        # 다음 칸이 더 낮은 경우 (오른쪽에 경사로 설치 필요)
        if temp[idx] > temp[idx + 1]:
            if not next_node_small(idx, temp, visited):
                return False
            idx += l  # 경사로 설치 후 다음 위치로 이동

        # 다음 칸이 더 높은 경우 (왼쪽에 경사로 설치 필요)
        else:
            if not next_node_big(idx, temp, visited):
                return False
            idx += 1  # 경사로 설치 후 다음 위치로 이동

    return True


def next_node_small(idx, temp, visited):
    node = temp[idx + 1]

    # 경사로 범위 확인
    if idx + 1 + l > n:
        return False

    for i in range(idx + 1, idx + 1 + l):
        if visited[i] or temp[i] != node:
            return False
        visited[i] = True  # 경사로 설치 표시

    return True


def next_node_big(idx, temp, visited):
    node = temp[idx]

    # 경사로 범위 확인
    if idx + 1 - l < 0:
        return False

    for i in range(idx, idx - l, -1):
        if visited[i] or temp[i] != node:
            return False
        visited[i] = True  # 경사로 설치 표시

    return True


# 입력 및 전체 탐색
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 가로 줄 검사
for i in range(n):
    if solution(i, False):
        cnt += 1

# 세로 줄 검사
for i in range(n):
    if solution(i, True):
        cnt += 1

print(cnt)
