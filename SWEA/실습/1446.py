# 1. 내장 함수를 활용하여 리스트 내 최대값을 산출하자!
def find_min_max(req):
    return (max(req), min(req))

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

# 1. 내장 함수를 활용하지 않고 리스트 내 최대값을 산출하자!
def find_min_max(req):
    max = 0
    min = req[0]
    for num in req:
        if num > max:
            max = num
        if num < min:
            min = num
    return (max, min)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
