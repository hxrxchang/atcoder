N = int(input())
A = list(map(int, input().split()))

dic = dict()
for a in A:
  if not a in dic.keys():
    dic[a] = 1
  else:
    dic[a] += 1

cnt = 0
for k in dic.keys():
  cnt += dic[k] // 2

print(cnt)
