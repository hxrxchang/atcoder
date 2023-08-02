N, K = map(int, input().split())
A = list(map(int, input().split()))

counts = []
# counts_set = set()
for i in range(2 ** N):
  cnt = 0
  for j in range(N):
    if (i >> j) & 1:
      cnt += A[j]
  # if not cnt in counts_set:
  counts.append(cnt)
    # counts_set.add(cnt)

counts.sort()

print(len(counts))
print(counts[K - 1])
