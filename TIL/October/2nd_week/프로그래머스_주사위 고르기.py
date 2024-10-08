import itertools


def binary_search(now, other_case):
    low = 0
    high = len(other_case) - 1

    while low <= high:
        mid = (low + high) // 2

        if other_case[mid] < now:
            low = mid + 1
        else:
            high = mid - 1
    return low


def dfs(case, dice, depth, now, res):
    # 깊이(더한 주사위들의 갯수)가 case의 길이와 같다면 리턴 case의 길이: 각 경우의 수
    if len(case) == idx:
        res.append(now)
        return
    dice_idx = case[idx]
    for d in dice[dice_idx]:
        dfs(case, dice, depth + 1, now + d, res)


def solution(dice):
    answer = []
    half = len(dice) // 2
    li = [i for i in range(len(dice))]
    # 주사위를 선택할 수 있는 조합의 경우를 찾기
    cases = list(itertools.combintations(li, 3))

    sum_cases = {}

    for idx, case in enumerate(cases):
        res = []
        # 주사위들의 합
        dfs(case, dice, 0, 0, res)
        # 바이너리 서치를 위해 정렬
        res.sort()
        # 인덱스를 키로 저장 cases에서 값을 가져오기 위함 
        sum_cases[idx] = res
    max_sum = 0
    case_len = len(cases)
    for idx, value in sum_cases.items():
        # 나
        my_case = value
        # 상대방 반대편이므로
        ohter_case = sum_cases[case_len - 1 - idx]

        temp_sum = 0
        for num in my_case:
            temp_sum += binary_search(num, ohter_case)

    return answer
