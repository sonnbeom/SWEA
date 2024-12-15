def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    # 첫번째 인자는 내림차순, 두번째 인자는 오름차순(같다면)
    scores.sort(key=lambda score: (-score[0], score[1]))
    max_second = 0
    rank = 1

    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        # 첫번째 숫자보다 작음 + 두번째 숫자는 크거나 같아야 배제 대상이 아님
        if max_second <= score[1]:
            if wanho_sum < score[0] + score[1]:
                rank += 1
            max_second = score[1]
    return rank
