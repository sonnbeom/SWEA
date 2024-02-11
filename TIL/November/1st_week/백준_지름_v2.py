from collections import defaultdict

def dfs(start, node, num):

    global temp_num
    if len(dic[node]) == 0:
        temp_num = max(temp_num, num)
        return
    for li in dic[node]:
        next_node = li[0]
        cost = li[1]
        num += cost
        dfs(start, next_node, num)
        num -= cost

dic = defaultdict(list)
node_cnt = int(input())
max_node = 0

for _ in range(node_cnt-1):
    p_node, c_node, cost = map(int, input().split())
    dic[p_node].append((c_node, cost))
    max_node = max(max_node, p_node, c_node)
    dic[p_node]
    dic[c_node]

score = [0 for _ in range(max_node+1)]
for i in dic:
    if len(dic[i]) > 0:
        temp_list = []
        for child in dic[i]:
            child_node = child[0]
            child_cost = child[1]
            temp_num = 0
            if len(dic[child_node]) >= 1:
                dfs(child_node, child_node, 0)
                max_cost = child_cost + temp_num
                temp_list.append(max_cost)
            else:
                temp_list.append(child_cost)
        if len(temp_list) > 0:
            temp_list.sort(reverse=True)
            t = temp_list.pop(0)
            score[i] += t
            if len(temp_list) > 0:
                t = temp_list.pop(0)
                score[i] += t
print(max(score))

