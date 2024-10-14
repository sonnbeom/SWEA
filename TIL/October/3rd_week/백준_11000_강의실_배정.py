import heapq
# def func(tmp_list):
#     global cnt
#     cnt += 1
#     end, start = heapq.heappop(hq)
#     now_end = end
#     while hq:
#         end, start = heapq.heappop(hq)
#         if not (now_end <= start):
#             tmp_list.append((end, start))
#             continue
#         if not (end >= now_end):
#             tmp_list.append((end, start))
#             continue
#         now_end = end


n = int(input())
hq = []

for _ in range(n):
    a, b = map(int, input().split())
    data = [b, a]
    hq.append(data)

heapq.heapify(hq)

cnt = 0
while hq:
    tmp_list = []
    end, start = heapq.heappop(hq)
    now_end = end
    while hq:
        end, start = heapq.heappop(hq)
        if not (now_end <= start):
            tmp_list.append((end, start))
            continue
        if not (end >= now_end):
            tmp_list.append((end, start))
            continue
        now_end = end
    for e_time, s_time in tmp_list:
        heapq.heappush(hq, (e_time, s_time))
    cnt += 1

print(cnt)

