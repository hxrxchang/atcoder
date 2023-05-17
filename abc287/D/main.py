S = list(input())
T = list(input())

def match(x, y):
  return x == y or x == '?' or y == '?'

# pre[i] = S[:i] と T[:i] が一致するか
pre = [False] * (len(S) + 1)
pre[0] = True

for i in range(len(T)):
  if match(S[i], T[i]):
    pre[i + 1] = True
  else:
    break

S_ = list(reversed(S))
T_ = list(reversed(T))
# suf[i] = S[-i:] と T[-i:] が一致するか
suf = [False] * (len(S) + 1)
suf[0] = True
for i in range(len(T)):
  if match(S_[i], T_[i]):
    suf[i + 1] = True
  else:
    break

for i in range(len(T) + 1):
  if pre[i] and suf[len(T) - i]:
    print('Yes')
  else:
    print('No')
