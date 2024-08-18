arr = ' 12345678'


def postorder(now):
    if now > len(arr) - 1: return
    postorder(now * 2)
    postorder(now * 2 + 1)
    print(arr[now], end=' ')  # 후위 순회니깐 뒤에 print()


postorder(1)  # 후위순회