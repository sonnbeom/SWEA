import itertools

n = int(input())
player = []
for i in range(n):
    temp = list(map(int, input().split()))
    player.append(temp)

# 순열을 생성하여 1번 타자를 고정으로 설정
permutation = itertools.permutations(range(1, 9), 8)

answer = 0
for p in permutation:
    p = list(p)
    score = 0
    seq = 0

    # 1번 타자를 고정하여 타순 재구성
    bat = p[:3] + [0] + p[3:]
    print(f'bat = {bat}')

    for i in range(n):  # 각 이닝에 대해 시뮬레이션
        out = 0
        p1 = p2 = p3 = home = 0  # 주자 초기화

        while out < 3:  # 아웃이 3번 날 때까지 진행
            a = bat[seq]  # 현재 타자의 순번
            b = player[i][a]  # 현재 타자의 결과
            print(f'out ={out}')
            print(f'b ={b} i = {i}')

            if b == 0:  # 아웃인 경우
                out += 1  # 아웃 카운트를 증가시킴
            elif b == 1:  # 1루타
                home += p3  # 3루 주자가 홈으로 들어옴
                score += home
                p3 = home = 0  # 홈과 3루 상태 초기화
                p3 += p2  # 2루 주자를 3루로 이동
                p2 = 0
                p2 += p1  # 1루 주자를 2루로 이동
                p1 = 1  # 현재 타자는 1루로 진출
            elif b == 2:  # 2루타
                home += p3 + p2  # 3루, 2루 주자가 홈으로 들어옴
                score += home
                p3 = home = 0  # 홈과 3루 상태 초기화
                p3 += p1  # 1루 주자를 3루로 이동
                p1 = 0
                p2 = 1  # 현재 타자는 2루로 진출
            elif b == 3:  # 3루타
                home += p3 + p2 + p1  # 모든 주자가 홈으로 들어옴
                score += home
                p1 = p2 = home = 0  # 홈과 모든 주자 상태 초기화
                p3 = 1  # 현재 타자는 3루로 진출
            else:  # 홈런
                home += p3 + p2 + p1 + 1  # 모든 주자와 타자가 홈으로 들어옴
                score += home
                home = 0  # 홈 상태 초기화

            seq += 1  # 다음 타순으로 이동
            if seq == 9:  # 타순이 9번 타자를 넘어가면
                seq = 0  # 다시 1번 타자로 순환

        # 문제점 1: home 변수는 주자의 이동 및 점수 계산과 중복된 역할을 함.
        # 문제점 2: 특정 조건에서 p1, p2, p3를 제대로 초기화하지 않아
        #          다음 루프에서 남아 있는 주자 상태로 인해 무한 루프 발생 가능.
        # 문제점 3: b == 0인 경우 외에는 out이 증가하지 않으므로,
        #          타자가 계속 진루하여 점수만 쌓이는 비정상적인 시나리오가 발생.

    answer = max(answer, score)  # 최대 점수를 갱신

print(answer)  # 최종 답안 출력