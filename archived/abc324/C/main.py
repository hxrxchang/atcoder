N, T = list(input().split())
N = int(N)
S = [input() for _ in range(N)]

ans = []

def check(S, T):
  # パターン1: 同じ
  if S == T:
    return True
  else:
    if abs(len(S) - len(T)) > 1:
      return False
    # パターン2: 挿入
    elif len(T) - len(S) == 1:
      cnt = 0
      for i in range(len(S)):
        if T[i + cnt] != S[i]:
          if i + cnt + 1 < len(T) and T[i + cnt + 1] == S[i]:
            if cnt == 0:
              cnt += 1
              continue
            else:
              return False
          else:
            return False
      return True
    # パターン3: 削除
    elif len(S) - len(T) == 1:
      cnt = 0
      for i in range(len(T)):
        if S[i + cnt] != T[i]:
          if i + cnt + 1 < len(S) and S[i + cnt + 1] == T[i]:
            if cnt == 0:
              cnt += 1
              continue
            else:
              return False
          else:
            return False
      return True
    # パターン4: 置換
    else:
      cnt = 0
      for i in range(len(S)):
        if S[i] != T[i]:
          if cnt == 0:
            cnt += 1
            continue
          else:
            return False
      return True

for i, s in enumerate(S):
  if check(s, T):
    ans.append(i + 1)

print(len(ans))
print(*ans)
