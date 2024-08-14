one = list(map(int, input()))
two = list(map(int, input()))
thr = list(map(int, input()))
four = list(map(int, input()))

k = int(input())
oneIdx = 2
twoIdx = [6, 2]
thrIdx = [6, 2]
fourIdx = 6

def solutionOne(d):
    global oneIdx, twoIdx, thrIdx, fourIdx
    if d == 1:
        r = one[oneIdx]
        oneIdx = (oneIdx - 1) % 8
        if two[twoIdx[0]] != r:
            r = two[twoIdx[1]]
            twoIdx[0] = (twoIdx[0] + 1) % 8
            twoIdx[1] = (twoIdx[1] + 1) % 8
            if thr[thrIdx[0]] != r:
                r = thr[thrIdx[1]]
                thrIdx[0] = (thrIdx[0] - 1) % 8
                thrIdx[1] = (thrIdx[1] - 1) % 8
                if r != four[fourIdx]:
                    fourIdx = (fourIdx + 1) % 8
    else:
        r = one[oneIdx]
        oneIdx = (oneIdx + 1) % 8
        if two[twoIdx[0]] != r:
            r = two[twoIdx[1]]
            twoIdx[0] = (twoIdx[0] - 1) % 8
            twoIdx[1] = (twoIdx[1] - 1) % 8
            if thr[thrIdx[0]] != r:
                r = thr[thrIdx[1]]
                thrIdx[0] = (thrIdx[0] + 1) % 8
                thrIdx[1] = (thrIdx[1] + 1) % 8
                if r != four[fourIdx]:
                    fourIdx = (fourIdx - 1) % 8

def solutionTwo(d):
    global oneIdx, twoIdx, thrIdx, fourIdx
    if d == 1:
        l = two[twoIdx[0]]
        r = two[twoIdx[1]]
        twoIdx[0] = (twoIdx[0] - 1) % 8
        twoIdx[1] = (twoIdx[1] - 1) % 8
        if l != one[oneIdx]:
            oneIdx = (oneIdx + 1) % 8
        if r != thr[thrIdx[0]]:
            r = thr[thrIdx[1]]
            thrIdx[0] = (thrIdx[0] + 1) % 8
            thrIdx[1] = (thrIdx[1] + 1) % 8
            if r != four[fourIdx]:
                fourIdx = (fourIdx - 1) % 8
    else:
        l = two[twoIdx[0]]
        r = two[twoIdx[1]]
        twoIdx[0] = (twoIdx[0] + 1) % 8
        twoIdx[1] = (twoIdx[1] + 1) % 8
        if l != one[oneIdx]:
            oneIdx = (oneIdx - 1) % 8
        if r != thr[thrIdx[0]]:
            r = thr[thrIdx[1]]
            thrIdx[0] = (thrIdx[0] - 1) % 8
            thrIdx[1] = (thrIdx[1] - 1) % 8
            if r != four[fourIdx]:
                fourIdx = (fourIdx + 1) % 8
def solutionThr(d):
    global oneIdx, twoIdx, thrIdx, fourIdx
    if d == 1:
        l = thr[thrIdx[0]]
        r = thr[thrIdx[1]]
        thrIdx[0] = (thrIdx[0] - 1) % 8
        thrIdx[1] = (thrIdx[1] - 1) % 8
        if r != four[fourIdx]:
            fourIdx = (fourIdx + 1) % 8
        if l != two[twoIdx[1]]:
            l = two[twoIdx[0]]
            twoIdx[0] = (twoIdx[0] + 1) % 8
            twoIdx[1] = (twoIdx[1] + 1) % 8
            if l != one[oneIdx]:
                oneIdx = (oneIdx - 1) % 8

    else:
        l = thr[thrIdx[0]]
        r = thr[thrIdx[1]]

        thrIdx[0] = (thrIdx[0] + 1) % 8
        thrIdx[1] = (thrIdx[1] + 1) % 8

        if r != four[fourIdx]:
            fourIdx = (fourIdx - 1) % 8

        if l != two[twoIdx[1]]:
            l = two[twoIdx[0]]
            twoIdx[0] = (twoIdx[0] - 1) % 8
            twoIdx[1] = (twoIdx[1] - 1) % 8
            if l != one[oneIdx]:
                oneIdx = (oneIdx + 1) % 8

def solutionFour(d):
    global oneIdx, twoIdx, thrIdx, fourIdx
    if d == 1:
        l = four[fourIdx]
        fourIdx = (fourIdx - 1) % 8
        if thr[thrIdx[1]] != l:
            l = thr[thrIdx[0]]
            thrIdx[0] = (thrIdx[0] + 1) % 8
            thrIdx[1] = (thrIdx[1] + 1) % 8
            if two[twoIdx[1]] != l:
                l = two[twoIdx[0]]
                twoIdx[0] = (twoIdx[0] - 1) % 8
                twoIdx[1] = (twoIdx[1] - 1) % 8
                if l != one[oneIdx]:
                    oneIdx = (oneIdx + 1) % 8
    else:
        l = four[fourIdx]
        fourIdx = (fourIdx + 1) % 8
        if thr[thrIdx[1]] != l:
            l = thr[thrIdx[0]]
            thrIdx[0] = (thrIdx[0] - 1) % 8
            thrIdx[1] = (thrIdx[1] - 1) % 8
            if two[twoIdx[1]] != l:
                l = two[twoIdx[0]]
                twoIdx[0] = (twoIdx[0] + 1) % 8
                twoIdx[1] = (twoIdx[1] + 1) % 8
                if l != one[oneIdx]:
                    oneIdx = (oneIdx - 1) % 8
for i in range(k):
    idx, direc = map(int, input().split())
    if idx == 1:
        solutionOne(direc)
    elif idx == 2:
        solutionTwo(direc)
    elif idx == 3:
        solutionThr(direc)
    else:
        solutionFour(direc)
ans = 0
if one[oneIdx-2] == 1:
    ans += 1
if two[twoIdx[1]-2] == 1:
    ans += 2
if thr[thrIdx[1]-2] == 1:
    ans += 4
if four[fourIdx-6] == 1:
    ans += 8
print(ans)

