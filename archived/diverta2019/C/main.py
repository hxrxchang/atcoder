N = int(input())

cnt = 0
start_b_last_a = 0
last_a = 0
start_b = 0

for i in range(N):
  s = input()
  c = s.count("AB")
  cnt += c
  if s[0] == "B" and s[-1] == "A":
    start_b_last_a += 1
    continue
  if s[0] == "B":
    start_b += 1
  if s[-1] == "A":
    last_a += 1

if last_a == 0 and start_b == 0:
  cnt = cnt + max(start_b_last_a - 1, 0)
else:
  cnt = cnt + start_b_last_a + min(last_a, start_b)

print(cnt)

