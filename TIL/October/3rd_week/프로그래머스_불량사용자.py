def is_black_user(users, ban_id):
    res = 0
    for user in users:

        if len(user) != len(ban_id):
            continue
        check = 0
        for i in range(len(user)):
            if ban_id[i] == "*":
                continue
            elif ban_id[i] != user[i]:
                check += 1
                break
        if check == 0:
            res += 1
    return res


def solution(user_id, banned_id):
    cnt = []
    temp_set = set(banned_id)
    black_list = list(temp_set)
    for ban_user in black_list:
        res = is_black_user(user_id, ban_user)
        print(f'res = {res} ban_user = {ban_user}')
        if res != 0:
            cnt.append(res)

    answer = 0

    if len(cnt) == 0:
        return answer
    if len(cnt) == 1:
        answer = 1
    else:
        answer = cnt.pop(0)
        for num in cnt:
            answer *= num

    return answer