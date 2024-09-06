price = list(map(int,input().split()))
month = list(map(int,input().split()))

min_cost = price[-1]

def backtracking(cost, depth):
    global min_cost
    if depth > 11:
        min_cost = min(min_cost, cost)
        return
    if cost >= min_cost:
        return
    #3달 결제
    backtracking(cost+price[2], depth+3)
    #하루 결제
    one_day_cost = price[0] * month[depth]
    backtracking(cost+one_day_cost, depth+1)
    #한달치 결제
    backtracking(cost+price[1], depth+1)

    # 1일 이용권으로 결제, 한달 이용권으로 결제, 3달이용권으로 비용 각 비용을 더해서 호출한다.

backtracking(0,0)
print(min_cost)