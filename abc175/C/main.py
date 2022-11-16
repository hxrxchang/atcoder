X, K, D = map(int, input().split())

def main(first_position, times, distance):
  if first_position - distance * times >= 0:
    return first_position - distance * times
  remain = first_position % distance
  quotient = first_position // distance
  if (K - quotient) % 2 == 0:
    return remain
  else:
    return abs(remain - D)

ans = main(abs(X), K, D)
print(ans)
