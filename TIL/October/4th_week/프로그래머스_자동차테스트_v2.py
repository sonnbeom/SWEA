import sys
from itertools import combinations
from collections import defaultdict
n, q = map(int, input().split())
arr = list(map(int, input().split()))
mid_list = []
for _ in range(q):
    i = int(input())
    mid_list.append(i)

combination_list = list(combinations(arr, 3))
dic = defaultdict(int)
for combination in combination_list:
    combination = list(combination)
    combination.sort()
    mid = combination[1]
    dic[mid] += 1

for mid in mid_list:
    print(dic[mid])