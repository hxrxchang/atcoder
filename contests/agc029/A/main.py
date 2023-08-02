# 似てそうな問題
# https://atcoder.jp/contests/abc125/tasks/abc125_d
# https://atcoder.jp/contests/abc174/tasks/abc174_d

# 最終的に `BWBWBWBWB` が `WWWBBBB` になるようにすればいい
# つまり入力で得た文字列の各Wの要素を調べて、そのWより前にいるBの数を調べて合計する
S = input()
cnt = 0
b_cnt = 0
for i in range(len(S)):
  if S[i] == "W":
    cnt += b_cnt
  else:
    b_cnt += 1

print(cnt)
