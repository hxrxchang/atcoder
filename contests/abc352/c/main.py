N = int(input())

monsters = []

for i in range(N):
    A, B = map(int, input().split())
    diff = B - A
    monsters.append((A, B, diff))

monsters.sort(key=lambda x: x[2])

height = 0

for i, m in enumerate(monsters):
    A, B, diff = m
    height += B
    if i != 0 and diff != 0:
        height -= monsters[i - 1][2]

print(height)
