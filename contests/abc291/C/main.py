N = int(input())
S = input()

s = str(0) + ":" + str(0)
visited = {s}
current_x = 0
current_y = 0

for s in S:
  if s == "R":
    current_x += 1
  if s == "L":
    current_x -= 1
  if s == "U":
    current_y += 1
  if s == "D":
    current_y -= 1
  item = str(current_x) + ":" + str(current_y)
  if item in visited:
    print("Yes")
    exit()
  visited.add(item)

print("No")
