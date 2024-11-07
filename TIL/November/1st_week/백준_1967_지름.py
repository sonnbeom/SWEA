from collections import defaultdict

def dfs(start, node, num):
    global temp_num
    if len(dic[node]) == 0:
        score[start].append(num)
        temp_num = max(temp_num, num)
        return num
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
score = [[] for _ in range(max_node+1)]
score_list = [[0 for _ in range(max_node+1)] for _ in range(max_node+1)]

for i in dic:
    if len(dic[i]) > 0:
        for child in dic[i]:
            child_node = child[0]
            child_cost = child[1]
            temp_num = 0
            if len(dic[child_node]) > 1:
                dfs(child_node, child_node, 0)
                max_cost = child_cost + temp_num
                score_list[i][child_node] = max_cost
            else:
                score_list[i][child_node] = child_cost

answer = 0
for i in dic:
    if len(dic[i]) > 1:
        child_left = dic[i][0][0]
        child_right = dic[i][1][0]
        left_sum = score_list[i][child_left]
        right_sum = score_list[i][child_right]
        answer = max(answer, (left_sum + right_sum))
print(answer)