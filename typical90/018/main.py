from math import atan, cos, sin, pi

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

def calc(t):
  theta = 2 * pi * t / T
  height = L / 2 - L / 2 * cos(theta)
  y = -(L / 2 * sin(theta))
  dist = (X * X + (y - Y) ** 2) ** 0.5
  return atan(height / dist) / pi * 180

for _ in range(Q):
  e = int(input())
  print(calc(e))
