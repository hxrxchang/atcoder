N, K = map(int, input().split())
N-=1
K-=1
ans = N // K
if not N % K  == 0:
  ans+=1

print(ans)

