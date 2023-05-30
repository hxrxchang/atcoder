import math

N = int(input())

x0, y0 = map(int, input().split())
x_half, y_half = map(int, input().split())

# 中心座標
x_center = (x0 + x_half) / 2
y_center = (y0 + y_half) / 2

# 中心から各頂点までの距離
r = math.sqrt((x0 - x_center) ** 2 + (y0 - y_center) ** 2)

# 中心からx1, y1への角度
theta = math.atan2(y0 - y_center, x0 - x_center)

x1 = x_center + r * math.cos(theta + 2 * math.pi / N)
y1 = y_center + r * math.sin(theta + 2 * math.pi / N)

print(x1, y1)
