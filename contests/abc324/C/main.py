N, T = list(input().split())
N = int(N)
len_T = len(T)
S = [input() for _ in range(N)]

ans = []
for j, s in enumerate(S):
  # パターン1 同じ
  if s == T:
    ans.append(j + 1)
  else:
    len_s = len(s)
    if abs(len_s - len_T) > 1:
      continue
    # パターン2 挿入
    if len_T - len_s == 1:
      flag = True
      cnt = 0
      for i in range(len_s):
        if T[i + cnt] != s[i]:
          if i + cnt + 1 < len_T and T[i + cnt + 1] == s[i]:
            if cnt == 0:
              cnt += 1
              continue
            else:
              flag = False
              break
          else:
            flag = False
            break
      if flag:
        ans.append(j + 1)
    # パターン3 削除
    elif len_s - len_T == 1:
      flag = True
      cnt = 0
      for i in range(len_T):
        if s[i + cnt] != T[i]:
          if i + cnt + 1 < len_s and s[i + cnt + 1] == T[i]:
            if cnt == 0:
              cnt += 1
              continue
            else:
              flag = False
              break
          else:
            flag = False
            break
      if flag:
        ans.append(j + 1)
    # パターン4 置換
    elif len_s == len_T:
      flag = True
      cnt = 0
      for i in range(len_s):
        if s[i] != T[i]:
          if cnt == 0:
            cnt += 1
            continue
          else:
            flag = False
            break
      if flag:
        ans.append(j + 1)

print(len(ans))
print(*ans)
