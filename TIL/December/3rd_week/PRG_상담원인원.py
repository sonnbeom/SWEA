import itertools


# 가능한 조합을 추출하고 합을 체크한다.
def get_list(k, n):
    remaining = n - k + 2
    temp = list(itertools.product(range(1, remaining), repeat=k))
    res = []
    for t in temp:
        if sum(t) == n:
            res.append(t)
    return res


# pools를 만들어 각 idx별로 idx번 참가자의 끝나는 시간을 담는다.
# 경우의 수 3가지
# 1. 멘토가 가동되지 않은 경우 => 시작시간 + 상담시간 더해서 pools[idx] 갱신
# 2. 멘토가 가동됐으나 시간차가 발생하여 참가자 기다리지 않는 경우 => 시작시간 + 상담시간 더해서 pools[idx] 갱신
# 3. 멘토가 상담중인 경우 =>  가장 빨리 끝나는 멘토의 시간을 가져온다(정렬 사용) => reqs에서 시각과 멘토의 시간 차이를 반영
# 기다린 시간에 더하여 갱신 =>  멘토링 끝나는 시간과 상담 시간을 더하여 다시 pool에 더해준다.
# 4. 시간 초과를 고려하여 중간에 가지치기를 하여 시간 초과 방지
def func(li, reqs, k, minimum):
    pools = [[] for _ in range(k)]
    answer = 0

    for i in range(len(reqs)):
        if answer >= minimum:
            return minimum

        req = reqs[i]
        idx = req[2] - 1

        if li[idx] > 0:
            pools[idx].append(req[1] + req[0])
            li[idx] -= 1

        elif li[idx] <= 0:
            pools[idx].sort()
            pool = pools[idx].pop(0)

            if req[0] - pool >= 0:
                pools[idx].append(req[1] + req[0])
            else:
                diff = abs(req[0] - pool)
                answer += diff
                end = req[1] + pool
                pools[idx].append(end)
    return answer


# 조합을 만들고 최솟값을 알기 위한 함수
def solution(k, n, reqs):
    trial = get_list(k, n)
    minimum = int(1e9)
    for i in range(len(trial)):
        res = func(list(trial[i]), reqs, k, minimum)
        minimum = min(res, minimum)
    return minimum