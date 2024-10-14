'''

만약 완탐이라면
시간복잡도 = n + n-1 + n-2.... = n(n+1)/2
O(n**)
10000 * 10000 = 1억 = 10의 8승

보통 10의 6승 ~ 10의 8승
고로 불가능한 경우가 존재한다!

1. 처음과 끝 숫자 차이가 크지 않아야 한다.
규칙 : 작은 순서대로 좌 우 끝에 존재한다.

2. 배열의 순서대로 역순 배열과 일반 배열에 담는다.
3. 역순 배열을 뒤집고 일반 배열에 넣으면 완성
'''
t = int(input())
res = []
for tc in range(t):

    tmp_list = []
    reverse_list = []

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    while True:

        if len(arr) == 0:
            break
        tmp_list.append(arr.pop(0))

        if len(arr) == 0:
            break
        reverse_list.append(arr.pop(0))
        # 역순에 담아준다.

    reverse_list.reverse()
    # 4, 7, 9 이렇게 담기고 최종 배열에 담을 땐 9 7 4
    for r in reverse_list:
        tmp_list.append(r)

    answer = abs(tmp_list[0]-tmp_list[-1])

    for i in range(len(tmp_list)-1):
        diff = abs(tmp_list[i]-tmp_list[i+1])
        answer = max(answer, diff)
    res.append(answer)

for r in res:
    print(r)