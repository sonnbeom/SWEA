test = [[1,2,3], [4,5,6], [7,8,9]]

def rotate_90(req):
    n = len(req)
    rotate_list = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            rotate_list[x][n-1-y] = req[y][x]
    return rotate_list

print(rotate_90(test))

# 내장함수를 활용하여 시계방향으로 회전
func_rotate_list = list(map(list, zip(test[::-1])))
func_rotate_list2 = list(map(list, zip(*test[::-1])))
print(func_rotate_list)
print(func_rotate_list2)

for i in func_rotate_list:
    print(i[0])