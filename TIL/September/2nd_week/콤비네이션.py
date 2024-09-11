# import itertools
#
# arr = [1,2,3]
# t = itertools.combinations(arr, 2)
# print(list(t))

def dfs(depth, temp):
    global trial_list
    if depth == n:
        trial_list.append(temp.copy())
        return
    for i in range(w):
        temp.append(i)
        dfs(depth+1, temp)
        temp.pop()

n = 3

trial_list = []
w = 9
dfs(0,[])
print(trial_list)