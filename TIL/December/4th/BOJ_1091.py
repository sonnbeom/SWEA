# 2 0 1을 1 2 0 순서에 맞게 해야하므로 card[i]를 seq[i]의 순서로 넣는다
# ex) card = [2, 0 ,1] seq = [1, 2, 0] 2가 idx 1번이므로
# response [1] (여기서 1은 seq[0]이다) = card[0]
def transfer(card, n, seq):
    response = [0 for _ in range(n)]
    for i in range(n):
        response[seq[i]] = card[i]

    return response

n = int(input())
card = list(map(int, input().split()))
seq = list(map(int, input().split()))

#정답 set 시간 복잡도 1을 위해
answer_card = [0, 1, 2] * (n // 3)
answer = set()
answer.add(tuple(answer_card))

# 방문 배열 방문한 곳에 또 방문한다면 불가능이므로 -1 리턴
visited = set()
shuffle = 0

while True:
    # 정답인지 체크
    if tuple(card) in answer:
        break

    # 방문한 곳이지 체크
    elif tuple(card) in visited:
        shuffle = -1
        break

    #방문 체크
    visited.add(tuple(card))
    #카드 셔플
    card = transfer(card, n, seq)
    shuffle += 1

print(shuffle)