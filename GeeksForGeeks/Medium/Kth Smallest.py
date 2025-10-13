import heapq


def kthSmallest(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, -num)
        if (len(heap) > k):
            heapq.heappop(heap)
    return -heap[0]


def sort(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    return [heapq.heappop(heap) for _ in range(len(heap))]


arr = [2, 3, 1, 20, 15]
k = 4

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest(arr, k))

print(sort(arr))
