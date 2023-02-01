N = int(input())

hour = str(N // 3600)
N %= 3600
minute = str(N // 60)
N %= 60
second = str(N)

if len(hour) == 1:
  hour = "0" + hour
if len(minute) == 1:
  minute = "0" + minute
if len(second) == 1:
  second = "0" + second
ans = hour + ":" + minute + ":" + second
print(ans)
