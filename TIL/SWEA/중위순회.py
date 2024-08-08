def in_order(v):
	# 0번 정점이 없으므로, 0번은 자식이 없는 경우를 표시
    if v:
    	# 왼쪽 자식
        in_order(ch1[v])
        print(tree[v],end='') # visit(v)
        # 오른쪽 자식
        in_order(ch2[v])

# 완전 이진 트리
for tc in range(1):
    # 정점의 총 수
    last = int(input())

    # 완전 이진 트리 만들기
    tree = [0]*(last+1)
    # 왼쪽 자식
    ch1 = [0]*(last+1)
    # 오른쪽 자식
    ch2 = [0]*(last+1)

    for _ in range(last):
        s = input().split()
        # s[0] : 노드 번호, s[1] : 알파벳
        tree[int(s[0])] = s[1]
        
        # 왼쪽 자식이 있다면
        if len(s) >= 3:
        	# s[2] : 왼쪽 자식 노드 번호
            ch1[int(s[0])] = int(s[2])
            
        # 오른쪽 자식이 있다면
        if len(s) == 4:
        	# s[3] : 오른쪽 자식 노드 번호
            ch2[int(s[0])] = int(s[3])
            
    print(f'#{tc} ',end='')
    in_order(1)
    print()