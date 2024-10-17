from collections import deque

def solution(s,t):
    global is_can
    q = deque()
    q.append(t)

    while q:
        node = q.popleft()
        if len(node) == len(s):
            if node == s:
                is_can = 1
                q.clear()
                break
        else:
            if node[-1] == "A":
                node.pop(-1) # q.append(node[:-1])
                q.append(node)
            elif node[-1] == "B":
                node.pop(-1) # temp = node[:-1]
                node.reverse() # q.append(temp[::-1])
                q.append(node)


s = input()
t = list(input())

is_can = 0
solution(s, t)
print(is_can)