n = int(input())
arr = list(map(int, input().split()))

arr_sum = sum(arr)

# 물뿌리개 총 횟수는 3의 배수여야 함
if arr_sum % 3 != 0:
    print("NO")
    exit()

# 물뿌리개 2번을 사용할 수 있는 횟수와 1번을 사용할 수 있는 횟수를 추적
one_cnt = 0
two_cnt = 0

for x in arr:
    one_cnt += x % 2  # 1로만 사용할 수 있는 횟수
    two_cnt += x // 2  # 2로 사용할 수 있는 횟수

# 물뿌리개 2개를 사용하는 것이 가능한지 체크
if two_cnt >= one_cnt and (two_cnt - one_cnt) % 3 == 0:
    print("YES")
else:
    print("NO")
