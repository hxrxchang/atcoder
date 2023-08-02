N = int(input())
A = list(map(int, input().split()))
B = [{'idx': i + 1, 'v': v } for i, v in enumerate(A)]
B.sort(key=lambda x: x['v'])

res = []
for b in B:
  res.append(b['idx'])

print(*res)
