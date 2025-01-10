def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    else:
        return parent[x]
def union(party, parent, person):
    a = find_parent(parent, person)
    b = find_parent(parent, person)

    if a in truth and b in truth:
        return
    elif a in truth:
        parent[b] = a
    elif b in truth:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth_num = truth.pop(0)
truth = set(truth)

parent = [i for i in range(n)]
parties = []
for i in range(m):
    party = list(map(int, input().split()))
    party_num = party.pop(0)
    for person in range(party_num-1):
        union(party, parent, person)
ans = 0
for party in parties:
    for i in range(len(party)-1):
        if find_parent(parent, party[i]) in truth:
            break
        else:
            ans += 1