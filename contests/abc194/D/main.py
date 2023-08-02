N = int(input())

ans = 0

# "有効なのが来るまでカードを引く期待値は、有効なカードを引く確率の逆数" と同じ考え方
for i in range(1, N):
  ans += N / (N - i)

print(ans)
