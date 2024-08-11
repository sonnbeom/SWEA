def dfs(start, depth, n, k, current_sum):
    global res
    if depth == n:  # N개의 원소를 선택했을 때
        if current_sum == k:  # 합이 K인지 확인
            res += 1
        return
    
    for i in range(start, 13):  # 1부터 12까지 반복
        dfs(i + 1, depth + 1, n, k, current_sum + i)

T = int(input("테스트 케이스 개수 입력: "))
for _ in range(T):
    res = 0
    n, k = map(int, input("N과 K 입력: ").split())
    dfs(1, 0, n, k, 0)  # 1부터 시작
    print(res)
