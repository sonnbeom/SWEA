from collections import defaultdict

def transfer(card, n, seq):
    response = [0 for _ in range(n)]
    for i in range(n):
        response[seq[i]] = card[i]

    return response

n = int(input())
card = list(map(int, input().split()))
seq = list(map(int, input().split()))
visited = set()
answer_card = [0, 1, 2] * (n // 3)
answer = set()
answer.add(tuple(answer_card))
shuffle = 0
while True:
    if tuple(card) in answer:
        break
    elif tuple(card) in visited:
        shuffle = -1
        break
    card = transfer(card, n, seq)
    shuffle += 1
    visited.add(tuple(card))

print(shuffle)