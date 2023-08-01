from collections import deque

H, W = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int(), input().split())
sh, sw, gh, gw = sh - 1, sw - 1, gh - 1, gw - 1

grid = [list(input()) for _ in range(H)]

dist = [[[0] * 4] * W for _ in range(H)]

def can_go(y, x):
  return 0 <= y < H and 0 <= x < W and grid[y][x] != '#'
