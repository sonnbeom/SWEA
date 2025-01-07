dy = [1,-1,0,0]
dx = [0,0,1,-1]
def is_range_valid(y, x):
    if 0 <= y < n and 0 <= x < n:
        return True
    else:
        return False
def find_near(like_list):
    near_arr = [[0 for _ in range(n)] for _ in range(n)]
    response = []
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if not is_range_valid(ny, nx):
                    continue
                if arr[ny][nx] in like_list:
                    near_arr[y][x] += 1
    max_num = 0
    if like_list[0] == 1 and like_list[1] == 3:
        print(f'near_arr ={near_arr}')
    for y in range(n):
        temp_max_num = max(near_arr[y])
        max_num = max(max_num, temp_max_num)
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                continue
            if near_arr[y][x] == max_num:
                response.append([y,x])
    return response

def find_most_empty(near_list):
    response = []
    empty_list = [[0 for _ in range(n)] for _ in range(n)]

    for y, x in near_list:
        if arr[y][x]:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not is_range_valid(ny, nx):
                continue
            if arr[ny][nx] == 0:
                empty_list[y][x] += 1
    max_empty = 0
    for i in range(n):
        temp_max_empty = max(empty_list[i])
        max_empty = max(temp_max_empty, max_empty)
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                continue
            if empty_list[y][x] == max_empty:
                response.append([y, x])
    return response

def find_small_num(empty_list):
    empty_list.sort()
    min_y = empty_list[0][0]
    x_list = []
    for e in empty_list:
        if e[0] == min_y:
            x_list.append(e[1])
    x_list.sort()
    return [min_y, x_list[0]]

def get_satisfied():
    answer = 0
    for y in range(n):
        for x in range(n):
            like_list = dic[arr[y][x]]
            student_count = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if not is_range_valid(ny, nx):
                    continue
                if arr[ny][nx] in like_list:
                    student_count += 1
            answer += get_score(student_count)
    return answer

def get_score(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i == 2:
        return 10
    elif i == 3:
        return 100
    elif i == 4:
        return 1000
n = int(input())
students = []
dic = {}
t = [[] for _ in range((n*n)+1)]
for _ in range(n*n):
    li = list(map(int, input().split()))
    students.append(li)
    # t[li[0]] = li[1:]
    dic[li[0]] = li[1:]

arr = [[0 for _ in range(n)] for _ in range(n)]
last = students[-1][0]
for student, o, t, th, f in students:
    like_list = [o, t, th, f]
    near_list = find_near(like_list)

    if len(near_list) > 1:
        empty_list = find_most_empty(near_list)

        if len(empty_list) > 1:
            small_num = find_small_num(empty_list)
            y = small_num[0]
            x = small_num[1]
            arr[y][x] = student
        else: # empty_list가 1개일
            y = empty_list[0][0]
            x = empty_list[0][1]
            arr[y][x] = student
    else: # near_list가 하나만 있다면!
        y = near_list[0][0]
        x = near_list[0][1]
        arr[y][x] = student
    print(f'student = {student} arr= {arr}')

print(f'arr={arr}')
answer = get_satisfied()

print(answer)
