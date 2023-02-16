import string

N, K = map(int, input().split())
S = input()

memo = []
alphabet_str = string.ascii_lowercase
for _ in range(N):
  memo.append({s: None for s in alphabet_str})

for i in range(N):
  target = S[i:]
  for j in range(len(target)):
    memo[i][target[j]] = j

pos = 0
last = N - K + 1
ans = ""
while len(ans) < K:
  item = memo[pos]
  temp_idx = item['a']
  temp_st = 'a'
  print(temp_idx, temp_st)
  for i in range(1, len(alphabet_str)):
    st = alphabet_str[i]
    target = item[st]
    if target != None and target < last and target < temp_idx:
      temp_idx = target
      temp_st = st
  ans += temp_st
  pos = pos + temp_idx + 1
  last += 1

print(ans)
