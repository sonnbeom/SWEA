def remove_zero():
    zero_cnt = 0
    for i in range(n):
        if arr[i] == 0:
            zero_cnt += 1
    if zero_cnt >= 1:
        for i in range(zero_cnt):
            arr.remove(0)
def is_can_one():
    global one_idx
    if arr[0] == 0:
        arr.pop(0)
    if arr[0] >= 1:
        one_idx = 0

def find_over_two():
    for i in range(last_idx, -1, -1):
        if arr[i] >= 2:
            return i
    return -10
def is_can_two():
    global two_cnt, two_idx
    if arr[-1] == 0:
        arr.pop(-1)
    idx = find_over_two()
    if idx != -10:
        two_idx = idx

def remove_by_idx():
    global one_cnt, two_cnt, last_idx

    if one_idx == -10:
        return
    if two_idx == -10:
        return

    #마지막 인덱스 먼저
    arr[two_idx] -= 2
    two_cnt -= 1

    if arr[two_idx] == 0:
        last_idx -= 1
    elif arr[two_idx] <= 1:
        last_idx -= 1

    arr[0] -= 1
    one_cnt -= 1

    if arr[0] == 0:
        arr.pop(0)


is_can = True
n = int(input())

arr = list(map(int, input().split()))

arr_sum = sum(arr)
if not(arr_sum >= 3 and arr_sum % 3 == 0):
    is_can = False

answer = "NO"

if is_can:
    remove_zero()
    arr.sort()
    while True:
        last_idx = len(arr) - 1
        one_idx = -10
        two_idx = -10
        one_cnt = 1
        two_cnt = 1
        if len(arr) <= 1:
            break
        is_can_one()

        is_can_two()

        remove_by_idx()
        if one_cnt == 1 or two_cnt == 1:
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr.remove(0)
            break
else:
    pass

if len(arr) == 1:
    if sum(arr) % 3 == 0:
        answer = "YES"

print(answer)
