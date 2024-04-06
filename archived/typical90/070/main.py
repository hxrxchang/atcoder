from statistics import median_low

n = int(input())
x = []
y = []

for _ in range(n):
  xi, yi = map(int, input().split())
  x.append(xi)
  y.append(yi)

x.sort()
y.sort()

ax = median_low(x)
ay = median_low(y)

ans_x = 0
ans_y = 0
for i in range(n):
  ans_x += abs(x[i] - ax)
  ans_y += abs(y[i] - ay)

print(ans_x + ans_y)
