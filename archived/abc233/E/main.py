X = [int(i) for i in list(input())]

nums = [0] * len(X)
nums[0] = X[0]

for i in range(1, len(X)):
  nums[i] = nums[i - 1] + X[i]

ans = [''] * len(X)
for i in range(len(X) - 1, 0, -1):
  nums[i - 1] += nums[i] // 10
  nums[i] %= 10
  ans[i] = str(nums[i])

ans[0] = str(nums[0])
print(''.join(ans))
