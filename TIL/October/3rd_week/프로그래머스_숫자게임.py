def is_win(team, other, visited, my_team_idx):
    res = [False]
    for i in range(my_team_idx, len(team)):
        if not visited[i] and team[i] > other:
            visited[i] = True
            res[0] = True
            res.append(i)
            return res
    return res
def solution(A, B):
    A.sort()
    B.sort()
    point = 0
    total_round = len(A)
    visited = [False for _ in range(total_round)]
    round = 0
    my_team_idx = 0
    while total_round > 0:
        if my_team_idx == len(A):
            break
        other = A[round]
        res = is_win(B, other, visited, my_team_idx)
        if res[0]:
            total_round -= 1
            round += 1
            point += 1
            my_team_idx = res[1]
        else:
            break
    print(point)
    return point