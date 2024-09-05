test = [[1,2,3], [4,5,6], [7,8,9]]

#내장 함수 사용 x
def rotate(req):
    n = len(req)
    tmp = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            tmp[x][n-1-y] = req[y][x]
    return tmp

# 내장함수 사용
print(rotate(test))
func_rotate_list = list(map(list, zip(*test[::-1])))
print(func_rotate_list)