def get_min_num(req_set, min_len, gems, idx):
    res = [False]
    temp = set()
    cnt = 0
    for i in range(idx, len(gems)):
        temp.add(gems[i])
        cnt += 1
        if cnt >= min_len:
            return res
        if len(temp) == len(req_set):
            res[0] = True
            res.append(i)

            return res
    return res


def solution(gems):
    answer = [0, len(gems)]
    req_set = set(gems)
    my_list = list(req_set)
    cnt = len(gems)
    for i in range(len(gems)):
        res = get_min_num(req_set, cnt, gems, i)
        if res[0]:
            cnt = res[1] - i + 1
            answer[0] = i
            answer[1] = res[1]
    answer[0] += 1
    if answer[1] != len(gems):
        answer[1] += 1

    return answer