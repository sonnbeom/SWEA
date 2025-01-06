def decide_degree(t, d):
    if t == 1:
        return -1 * d
    else:
        return d


def func(t, sy, sx, by, bx, d, board):
    d = decide_degree(t, d)
    for y in range(sy, by + 1):
        for x in range(sx, bx + 1):
            board[y][x] += d


def solution(board, skill):
    for t, sy, sx, by, bx, d in skill:
        func(t, sy, sx, by, bx, d, board)
    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 0:
                answer += 1
    return answer


