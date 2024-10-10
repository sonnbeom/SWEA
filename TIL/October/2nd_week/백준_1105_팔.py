'''
브루트포스
1. left의 숫자를 right와 같아질때까지 올린다.
2. 이 숫자의 길이를 기반으로 8이 몇개인지 체크한다.

시간을 줄여보자.
가장 처음에 숫자에서 8의 숫자를 계산한다.
1118 - > 1개
1
880
890
가지치기 조건
1. 만약 cnt가 0이라면 break
'''
def init():
    global left, right, flag, cnt
    while True:
        if cnt == 0:
            break

        elif left >= right:
            break

        str_left = str(left)
        if str_left[-1] == 8:
            var_cnt = get_count(left)
            cnt = min(var_cnt, cnt)
            flag = True
            break
        left += 1
        var_cnt = get_count(left)
        cnt = min(var_cnt, cnt)


def plus(num):
    global cnt, left
    left += num
    cnt = min(cnt, get_count(left))

def get_count(req):
    str_req = str(req)
    req_len = len(str_req)
    cnt = 0
    for i in range(req_len):
        if str_req[i] == "8":
            cnt += 1
    return cnt

left, right = map(int, input().split())

l_cnt = get_count(left)
r_cnt = get_count(right)

cnt = min(l_cnt, r_cnt)
flag = False

init()
is_two = True
while flag:
    if cnt == 0:
        break

    elif left >= right:
        break
    if is_two:
        plus(2)
        is_two = False
    else:
        plus(8)
        is_two = True



print(cnt)