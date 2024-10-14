l, r = input().split()

cnt = 0

# l과 r의 길이가 다르면 8을 비교할 필요가 없음
if len(l) == len(r):
    # 앞에서부터 하나씩 비교
    for i in range(len(l)):
        if l[i] == r[i] == '8':
            cnt += 1
        # 두 자릿수가 다르면 더 이상 8을 셀 필요가 없으므로 종료
        elif l[i] != r[i]:
            break

print(cnt)
