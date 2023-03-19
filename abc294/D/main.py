from heapq import heappop, heappush

N, Q = map(int, input().split())
tmp = 1

called = set()
for i in range(Q):
  E = list(map(int, input().split()))
  if E[0] == 1:
    called.add(tmp)
    tmp += 1
  elif E[0] == 2:
    called.remove(E[1])
  else:
    que = []
    heappush(que, list(called))
    print(heappop(que)[0])
