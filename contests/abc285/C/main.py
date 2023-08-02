S = input()

data = []
for s in list(S):
  data.append(ord(s) - 64)

data.reverse()

cnt = data[0]
for i in range(1, len(data)):
  cnt += 26 ** i * data[i]

print(cnt)

