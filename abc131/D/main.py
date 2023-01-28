N = int(input())
works = []
for _ in range(N):
  A, B = map(int, input().split())
  works.append((A, B))
# 締め切りが近い順にこなしていけばOKなのでその順番にソート
works.sort(key=lambda x: x[1])

current = 0
for work in works:
  current += work[0]
  if work[1] < current:
    print("No")
    exit()

print("Yes")
