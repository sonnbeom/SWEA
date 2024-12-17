import itertools


def get_list(k, n):
    remaining = n - k + 1
    temp = list(itertools.product(range(1, remaining), repeat=k))
    res = []
    for t in temp:
        if sum(t) == n:
            res.append(t)
    return res


def func(li, reqs, k, minimum):
    pools = [[] for _ in range(k + 1)]
    answer = 0
    for i in range(len(reqs)):
        if answer >= minimum:
            return minimum
        req = reqs[i]
        idx = req[2] - 1
        if li[idx] > 0:
            pools[idx].append(req[i])
            li[idx] -= 1
        elif li[idx] <= 0:
            pools[idx].sort(key=lambda a: a[1])
            pool = pools.pop(0)
            if req[0] - pool[1] >= 0:
                pools[idx].append(req)
            else:
                diff = abs(req[0] - pool[0])
                answer += diff
                pools[idx].append(req)


def solution(k, n, reqs):
    trial = get_list(k, n)
    minimum = int(1e9)
    for i in range(len(trial)):
        res = func(list(trial[i]), reqs, k, minimum)
        minimum = min(res, minimum)

    return minimum
k = 3
n = 5
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
solution(k, n, reqs)