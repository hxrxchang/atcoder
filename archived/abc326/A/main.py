X, Y = map(int, input().split())

diff = X - Y
if diff < 0 and diff < -2:
  print("No")
elif diff < 0 and diff >= -2:
  print("Yes")
elif diff >= 0 and diff > 3:
  print("No")
else:
  print("Yes")
