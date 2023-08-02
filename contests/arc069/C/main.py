N, M = map(int, input().split())

def solve(N, M):
  if N * 2 > M:
    return M // 2
  else:
    cnt = N
    M -= N * 2
    cnt += M // 4
    return cnt

ans = solve(N, M)
print(ans)

