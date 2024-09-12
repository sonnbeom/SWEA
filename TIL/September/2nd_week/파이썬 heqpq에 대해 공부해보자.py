import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 20)
heapq.heappush(heap, 10)
print(heap)

arr = [5,3,1]
heapq.heapify(arr)
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
# result = heapq.heappop(arr)
#
# print(arr)
# print(result)

