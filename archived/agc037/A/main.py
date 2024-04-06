S = input()

i = 0
ans = []
prev = ''
while i < len(S):
  # 末尾2文字の場合、同じだったらそれを追加
  if i == len(S) - 2:
    if S[i] == S[i + 1]:
      ans.append(S[i:i+2])
      break
  if S[i] != prev:
    ans.append(S[i])
    prev = S[i]
    i += 1
  else:
    ans.append(S[i:i+2])
    prev = S[i:i+2]
    i += 2

print(len(ans))
