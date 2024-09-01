import itertools

# 여러 개의 리스트가 들어있는 리스트
lists = [
    [0, 1, 2, 3],
    [[0, 1], [0, 2]],
    ['a', 'b', 'c']  # 예시로 추가된 세 번째 리스트
]

# itertools.product를 사용하여 모든 조합을 생성
combinations = list(itertools.product(*lists))

print(combinations)
