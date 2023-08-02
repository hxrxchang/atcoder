from collections import deque
from copy

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

que = deque()
que.append((1, 0))
que.append((0, 1))
pattern = [(0, 0)]




