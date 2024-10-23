def dfs(depth, start, temp):
    if depth == 3:  # 3개의 숫자를 고른 경우
        print(' '.join(map(str, temp)))  # 출력
        return

    for i in range(start, len(arr)):
        temp.append(arr[i])  # 현재 값을 temp에 추가
        dfs(depth + 1, i + 1, temp)  # 다음 값을 재귀적으로 탐색 (이후 값들만)
        temp.pop()  # 백트래킹: 마지막 값 제거

arr = [1, 2, 3, 4, 5]  # 숫자 배열
dfs(0, 0, [])  # DFS 시작, depth=0, start=0부터 시작
