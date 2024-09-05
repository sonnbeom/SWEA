test = [[1,2,3], [4,5,6], [7,8,9]]

def rotate_90(req):
    n = len(req)
    rorate_list = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            rorate_list[x][n-1-y] = req[y][x]

    return rorate_list

print(rotate_90(test))