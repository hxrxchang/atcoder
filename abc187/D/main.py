N = int(input())
towns = []
aoki_sum = 0
for _ in range(N):
  A, B = map(int, input().split())
  towns.append((A, B, A + B))
  aoki_sum += A

towns.sort(key=lambda x: x[2], reverse=True)

takahashi_sum = 0
for i, t in enumerate(towns):
  takahashi_sum += t[2]
  aoki_sum -= t[0]
  if takahashi_sum > aoki_sum:
    print(i + 1)
    break
