from collections import deque

S = input()
T = input()

que = deque()
for s in S:
    que.append(s)

ans = []

for i, t in enumerate(T):
    if que[0] == t:
        ans.append(i + 1)
        que.popleft()

print(*ans)
