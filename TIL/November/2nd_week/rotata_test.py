arr = []
arr.append([1,2,3])
arr.append([4,5,6])
arr.append([7,8,9])

def rotate(arr):
    list_tuple = zip(*arr[::-1])
    res = [list(e) for e in list_tuple]
    return res
#
# print(f'회전 전 arr = {arr}')
# res = rotate(arr)
# print(f'회전 후 res = {res}')


# 반시계 방향으로 90도 회전
rotated = list(zip(*arr))[::-1]
rotated = [list(row) for row in rotated]  # 튜플을 리스트로 변환
print(rotated)

a = 2.5
b = int(a)
print(b)