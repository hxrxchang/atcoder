N = int(input())
S = list(input())

c = S[0]
for i in range(1, N):
  if c == S[i]:
    print("No")
    exit()
  c = S[i]

print("Yes")

