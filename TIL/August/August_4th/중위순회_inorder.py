arr=' 12345678'

def inorder(now):
    if now > len(arr) - 1:
        print(f'now ={now} len = {len(arr)}')
        return
    inorder(now * 2)
    # print(arr[now], end=' ') # 중위 순회니깐 가운데에 print
    print(arr[now])
    inorder(now * 2 + 1)

inorder(1) # 중위순회