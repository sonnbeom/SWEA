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
                q.append(node[:-1])
            elif node[-1] == "B":
                temp = node[:-1]
                q.append(temp[::-1])


s = input()
t = input()

is_can = 0
solution(s, t)
print(is_can)