P, Q = input().split()

data = {
  'A': 0,
  'B': 3,
  'C': 4,
  'D': 8,
  'E': 9,
  'F': 14,
  'G': 23,
}

P = data[P]
Q = data[Q]

if P > Q:
  print(P - Q)
else:
  print(Q - P)
