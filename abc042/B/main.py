N, L = map(int, input().split())
S = [input() for _ in range(N)]
S.sort()

S2 = ""
for s in S:
  S2 += s

print(S2)
