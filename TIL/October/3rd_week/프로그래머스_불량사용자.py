def dfs(user_ids, depth, arr, answer):
    if depth == len(user_ids):
        arr.sort()
        temp = tuple(arr)
        answer.add(temp)
        return

    user_id = user_ids[depth]
    for u_id in user_id:
        if u_id not in arr:
            arr.append(u_id)
            dfs(user_ids, depth + 1, arr, answer)
            arr.remove(u_id)


def is_black_user(users, ban_id):
    res_user_list = []
    for user in users:

        if len(user) != len(ban_id):
            continue
        check = 0
        temp_user = user
        for i in range(len(user)):
            if ban_id[i] == "*":
                continue
            elif ban_id[i] != user[i]:
                check += 1
                break
        if check == 0:
            res_user_list.append(temp_user)
    return res_user_list


def solution(user_id, banned_id):
    possible_user_id = []
    for ban_user in banned_id:
        res_user_list = is_black_user(user_id, ban_user)
        if len(res_user_list) >= 1:
            possible_user_id.append(res_user_list)

    answer = set()
    dfs(possible_user_id, 0, [], answer)
    return len(answer)