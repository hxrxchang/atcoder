N = int(input())
S = list(input())

change_idx = []
in_mode = False
for i, s in enumerate(S):
  if s == '"':
    in_mode = not in_mode
  if s == ',' and not in_mode:
    change_idx.append(i)

for idx in change_idx:
  S[idx] = '.'

print(''.join(S))
