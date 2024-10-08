'''
첫번째 페이즈: 카드를 받을 때
1. 카드를 받으면 => n+1이 되는 카드가 있는지 체크한다. 되는 한쌍의 경우는 하나이다.
2. 즉 2개의 카드를 받았을 때 각각 13이 된다면 true를 리턴, 코인을 차감한다.
3. 만약 현재 내에서 없다면 tmp 리스트에 담아둔다. 추후에 사용할 수 있다.
두번째 페이즈: 카드를 제출할 때
1. 내 카드 내에서 제출한다.
2. 내 카드 1개와 tmp에 1개를 합쳐서 낸다
3. tmp 내에서 2개를 낸다.
'''

def is_valid(req, my_card, target):
    for card in my_card:
        if req + card == target:
            return True
    return False


def decide_coin_position(is_possible, req, my_card, tmp_card):
    coi = 0
    if is_possible:
        coi -= 1
        my_card.append(req)
    else:
        tmp_card.append(req)
    return coi


def can_sum_in_card(req_list, target):
    res = [False]
    if len(req_list) < 2:
        return res
    req_len = len(req_list)
    for i in range(req_len - 1):
        for j in range(i + 1, req_len):
            if req_list[i] + req_list[j] == target:
                res[0] = True
                res.append(req_list[i])
                res.append(req_list[j])
                break
    return res


def get_one_by_tmp(my_card, tmp_card, target, coin):
    res = [False]
    if len(tmp_card) < 1 and coin < 1:
        return res

    for card in my_card:
        for tmp in tmp_card:
            if card + tmp == target:
                res[0] = True
                res.append(card)
                res.append(tmp)
    return res


def solution(coin, cards):
    target = max(cards) + 1  # 타겟
    card_len = len(cards) // 3
    my_card = []  # 내가 보유하고 있는 카드
    for i in range(card_len):
        my_card.append(cards[0])
        cards.pop(0)
    tmp_card = []
    turn = 0
    coin = coin
    while True:
        turn += 1
        if len(cards) < 2:
            break
        card_one = cards.pop(0)
        card_two = cards.pop(0)
        if coin >= 1:  # 코인이 1개 이상 + 내 패와 합이 target인지 여부 확인
            res_valid = is_valid(card_one, my_card, target)
            res_coin = decide_coin_position(res_valid, card_one, my_card, tmp_card) #합이 target이라면 내 카드 리스트에 아니라면 tmp_card에
            if res_coin == -1: # 내 카드 리스트에 넣었다면 coin 차감
                coin -= 1

        if coin >= 1:
            res_valid = is_valid(card_two, my_card, target)
            res_coin = decide_coin_position(res_valid, card_two, my_card, tmp_card)
            if res_coin == -1:
                coin -= 1
        # 카드를 제출해보자 경우의 수 1. 내 카드 내 2개 2. 내 카드 1개/tmp 카드 1개 3. tmp 카드 2개
        res_my_card = can_sum_in_card(my_card, target) # 내 카드 내에서 2개를 낼 수 있는지 확인
        if res_my_card[0]:
            my_card.remove(res_my_card[1])
            my_card.remove(res_my_card[2])
        else:
            res_one_tmp = get_one_by_tmp(my_card, tmp_card, target, coin) # 내 카드 1개/tmp 카드 1개에서 낼 수 있는지 (코인이 적어도 하나 있어야 한다.)
            if res_one_tmp[0]:
                coin -= 1
                my_card.remove(res_one_tmp[0])
                tmp_card.remove(res_one_tmp[1])
            else:
                if coin >= 2: # tmp 카드 2개에서 낼 수 있는지 코인이 2개 이상어야 한다.
                    res_tmp_card = can_sum_in_card(tmp_card, target)
                    if res_tmp_card[0]:
                        tmp_card.remove(res_tmp_card[1])
                        tmp_card.remove(res_tmp_card[2])
                        coin -= 2
                    else:
                        break
                else:
                    break
    return turn

