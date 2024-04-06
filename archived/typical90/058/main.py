N, K = map(int, input().split())

# graph[i][0]: iの次の数
# graph[i][1]: iに何手で到達したか
graph = [[None, 0] for _ in range(10 ** 5)]

def sum_int(x):
  x = str(x)
  x_s = list(x)
  ans = 0
  for x_i in x_s:
    ans += int(x_i)
  return ans

tmp = N
cnt = 0
loop_period = None
while True:
  if graph[tmp][0] == None:
    next_int = (tmp + sum_int(tmp)) % 10 ** 5
    graph[tmp][0] = next_int
    graph[tmp][1] = cnt
    tmp = next_int
    cnt += 1
  else:
    loop_period = cnt - graph[tmp][1]
    break

if loop_period != None and cnt < K:
  K = cnt - loop_period + (K - cnt) % loop_period

tmp2 = N
for _ in range(K):
  tmp2 = graph[tmp2][0]

print(tmp2)
