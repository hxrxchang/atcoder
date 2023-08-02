N = int(input())
S = input()
T = input()

flags = []
for i in range(N):
  if S[i] == '1':
    if T[i] == 'l':
      flags.append(True)
      continue
  if T[i] == '1':
    if S[i] == 'l':
      flags.append(True)
      continue
  if S[i] == '0':
    if T[i] == 'o':
      flags.append(True)
      continue
  if T[i] == '0':
    if S[i] == 'o':
      flags.append(True)
      continue
  if S[i] == T[i]:
    flags.append(True)
    continue
  flags.append(False)

print('Yes' if False not in flags else 'No')

