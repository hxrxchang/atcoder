N = int(input())
V = list(map(int, input().split()))
V.sort()

while(len(V) >= 2):
  a, b = V[0:2]
  V.pop(0)
  V.pop(0)
  V.append((a + b) / 2)
  V.sort()

print(V[0])
