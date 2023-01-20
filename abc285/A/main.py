graph = {
  1: {"left": 2, "right": 3},
  2: {"left": 4, "right": 5},
  3: {"left": 6, "right": 7},
  4: {"left": 8, "right": 9},
  5: {"left": 10, "right": 11},
  6: {"left": 12, "right": 13},
  7: {"left": 14, "right": 15}
}

A, B = map(int, input().split())
if A > 7:
  print("No")
  exit()

target = graph[A]
if target["left"] == B or target["right"] == B:
  print("Yes")
else:
  print("No")
