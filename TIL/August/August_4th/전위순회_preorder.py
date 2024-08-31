arr = ' 12345678'  # arr[0] 은 비어있는 칸임


def preorder(now):
    if now > len(arr) - 1: return
    print(arr[now], end=' ')  # 전위 순회니깐 앞에 print()
    preorder(now * 2)  # 왼쪽 자식 노드 탐색
    preorder(now * 2 + 1)  # 오른쪽 자식 노드 탐색


preorder(1)  # 전위순회