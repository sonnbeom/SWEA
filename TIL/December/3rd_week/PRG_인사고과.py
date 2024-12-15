def is_valid(first, second, scores):
    sum_score = first + second
    rank = 1
    max_first = 0
    max_second = 0
    for i in range(len(scores)):
        score = scores[i]

        # 완호의 평가 점수가 모두 작은 경우
        if first < score[0] and second < score[1]:
            return -1

        # 두 평가 점수가 모두 작은 경우에 리턴
        if score[0] < max_first and score[1] < max_second:
            continue

        if sum_score < score[0] + score[1]:
            rank += 1

        if score[0] > max_first and score[1] > max_second:
            max_first = score[0]
            max_second = score[1]
    return rank


def solution(scores):
    temp = scores.pop(0)
    first = temp[0]
    second = temp[1]
    print(is_valid(first, second, scores))
    return is_valid(first, second, scores)


req = [[7, 1],[5, 4],[6, 6], [5, 4], [6, 6]]
solution(req)