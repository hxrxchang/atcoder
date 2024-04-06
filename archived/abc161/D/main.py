import heapq

K = int(input())
heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heapq.heapify(heap)

numbers = []
while True:
  item = heapq.heappop(heap)
  if item > 3234566667:
    break
  numbers.append(item)

  r = item % 10
  heapq.heappush(heap, item * 10 + r)
  if r != 0:
    heapq.heappush(heap, item * 10 + r - 1)
  if r != 9:
    heapq.heappush(heap, item * 10 + r + 1)

print(numbers[K - 1])


