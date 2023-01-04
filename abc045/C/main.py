S = input()
cnt = 0

# +を挿入できる箇所は数字の間だからlen(S) - 1
for i in range(2 ** (len(S) - 1)):
  temp = 0
  # 各桁をチェックする必要がある(1の位でbitが立つことはないが、計算に必要)
  for j in range(len(S)):
    if (i >> j) & 1:
      cnt += temp * 10 + int(S[j])
      temp = 0
    else:
      temp = temp * 10 + int(S[j])
  cnt += temp

print(cnt)
