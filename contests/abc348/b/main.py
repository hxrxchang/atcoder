import math

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x, y = points[i][0], points[i][1]
    diff = 0
    ans = 0
    for i in range(N):
        x2, y2 = points[i][0], points[i][1]
        diff2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
        if diff2 > diff:
            ans = i + 1
            diff = diff2
    print(ans)
