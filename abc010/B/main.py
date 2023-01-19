N = int(input())
flowers = list(map(int, input().split()))

cnt = 0
for flower in flowers:
  # 「好き」「嫌い」「大好き」の 3 つを繰り返しながら、花びらを1枚ずつ毟っていくパターン
  # 「好き」「嫌い」を交互に言いながら、花びらを 1 枚ずつ毟っていくパターン
  while flower % 3 == 2 or flower % 2 == 0:
    flower -= 1
    cnt += 1

print(cnt)
