arr = [
    [8, 2, 3],
    [3, 4, 5],
    [9, 3, 2]
]
arr2 =[
    [2, 3, 2, 5, 6],
    [8, 7, 2, 1, 3],
    [2, 3, 1, 4, 5],
    [4, 5, 1, 1, 1],
    [3, 2, 1, 4, 3]
]
# 반시계 방향으로 90도 회전
print(arr[::-1])
A = list(map(list, zip(*arr[::-1])))
print(A)
rotated = [list(row) for row in A]
print(rotated)
a = [
    [3,4,5],
    [6,7,8]
    ]
print(a[::-1])

a = list(map(list, zip(*arr2[::-1])))
print(a)