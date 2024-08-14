def dfs(arr, start, depth, current_comb, all_combinations):
    # 조합의 길이가 2인 경우
    if depth == 2:
        all_combinations.append(current_comb.copy())
        return

    # 현재 인덱스부터 시작하여 조합을 생성
    for i in range(start, len(arr)):
        # 현재 요소를 조합에 추가
        current_comb.append(arr[i])
        # 다음 요소를 선택하기 위해 재귀 호출
        dfs(arr, i + 1, depth + 1, current_comb, all_combinations)
        # 백트래킹: 현재 요소를 조합에서 제거
        current_comb.pop()

def get_combinations(arr):
    all_combinations = []
    dfs(arr, 0, 0, [], all_combinations)
    return all_combinations

# 사용 예시
arr = [1, 2, 3]
combinations = get_combinations(arr)
for comb in combinations:
    print(comb)
