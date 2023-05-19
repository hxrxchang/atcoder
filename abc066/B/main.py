S = list(input())

def ok(S):
  if len(S) % 2 != 0:
    return False
  for i in range(len(S) // 2):
    if S[i] != S[len(S) // 2 + i]:
      return False
  return True

while True:
  S.pop()
  if ok(S):
    print(len(S))
    break
