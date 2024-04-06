H, W, K = map(int, input().split())

graph = [input() for _ in range(H)]

ans = 0
for h in range(2 ** H):
  for w in range(2 ** W):
    black_cnt = 0
    for h2 in range(H):
      for w2 in range(W):
        # フラグが立っているということは、その行 or 列が赤くなるろいうことなので、フラグが立っていない場所に限定する
        if (h >> h2) & 1 == 0 and (w >> w2) & 1 == 0 and graph[h2][w2] == "#":
          black_cnt += 1
    if black_cnt == K:
      ans += 1

print(ans)
