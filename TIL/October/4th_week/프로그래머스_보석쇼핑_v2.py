from collections import deque


def solution(gems):
    left = 0
    right = 0
    temp = deque()
    req_set = set(gems)
    req_len = len(req_set)
    end_len = len(gems)
    storage = []
    is_right = True
    while right <= end_len:
        if len(temp) == 0 and len(storage) != 0:
            break
        if left == right and left != 0:
            break
        temp_set = set(temp)
        if len(temp_set) == req_len:
            diff = right - left
            storage.append((diff, left, right-1))
            temp.popleft()
            left += 1
        else:
            if is_right:
                temp.append(gems[right])
                right += 1
                if right >= end_len:
                    is_right = False
            else:
                temp.popleft()

    answer = []
    storage.sort()
    min_len = storage[0][0]
    for l, start, end in storage:
        if l == min_len:
            answer.append((start, end))
        else:
            break
    answer.sort()
    res = answer[0]
    answer = []
    for r in res:
        answer.append(r+1)
    return answer



req = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
req2 = ["AA", "AB", "AC", "AA", "AC"]
req3 = ["XYZ", "XYZ", "XYZ"]
req4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
res = solution(req4)
print(f'res = {res}')