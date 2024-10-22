from collections import defaultdict
def solution(gems):
    left = 0
    dic = defaultdict(int)
    req_set = set(gems)
    req_len = len(req_set)
    end_len = len(gems)
    answer = [0, end_len-1]
    min_len = end_len
    for right in range(end_len):
        next_node = gems[right]
        dic[next_node] += 1

        while len(dic) == req_len:
            # 짧은 구간 있다면 저장
            diff = right-left
            if diff < min_len:
                min_len = diff
                answer = [left, right]

            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]