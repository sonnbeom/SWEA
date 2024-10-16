def find_parent(now, parent):
    if parent[now] != now:
        parent[now] = find_parent(parent[now], parent)
    #여기서 else를 쓰면 안 된다 왜일까?
    return parent[now]
    '''
    3의 부모: 2
    2의 부모: 1
    1의 부모: 0 라고 가정
    find_parent(3, parent)를 호출
    2는 3과 같지 않으므로  find_parent(2, parent)
    1은 2와 같지 않으므로 find_parent(1, parent)
    0은 1과 같지 않으므로 find_parent(0, parent)
    0드디어 같다! 그렇다면 리턴 값은 어디로 가는 것인가? 
    이전에 호출한 함수로 가는 것이다. 즉
    parent[now] = find_parent(parent[now], parent) 여기로 오게 된다
    이렇게 되면 3,2,1 의 부모가 0으로 세팅되어서 이러한 반복 과정을 겪지 않아도 된다.
    
    앞선 과정을 해결한 경우는 다음과 같다.
    
    3의 부모: 0
    2의 부모: 0
    1의 부모: 0
    find_parent(3, parent) 호출 0 !=3 이므로 find_parent(0, parent)
    0은 0과 같으므로 0 리턴 고로 앞선 반복이 생략된다.
    '''


def union(a, b, parent): #부모를 갱신하는 함수
    a_parent = find_parent(a, parent)
    b_parent = find_parent(b, parent)

    if a_parent < b_parent: #노드 숫자가 작은 것이 가장 상위 노드
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def solution(n, costs):
    for cost in costs:
        temp_cost = cost.pop(-1) #비용을 정렬해야하므로 위 과정 반복
        cost.insert(0, temp_cost)

    costs.sort()
    parent = [i for i in range(n)]
    total_cost = 0
    for cost, start, end in costs:
        if find_parent(start, parent) != find_parent(end, parent): #부모가 같지 않다면 엣지가 연결되지 않은 것
            union(start, end, parent) #부모가 다르니 연결 해주고 비용 추가
            total_cost += cost
    return total_cost
