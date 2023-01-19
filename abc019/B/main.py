S = input()
S = list(S)

result = ''
char = S[0]
cnt = 1
for i in range(1, len(S)):
  if char == S[i]:
    cnt += 1
  else:
    result += char + str(cnt)
    char = S[i]
    cnt = 1

result += char + str(cnt)

print(result)

