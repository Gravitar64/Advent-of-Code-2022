# Based of https://www.reddit.com/user/OilAppropriate2827/
# Took only 0.4 ms for both parts!!!!!!

from time import perf_counter as pfc
import re


def read_puzzle(file):
  with open(file) as f:
    return [list(map(int, re.findall('\-?\d+', line))) for line in f.readlines()]


def solve(puzzle):
  maxi = 4_000_000
  data = [(sx, sy, abs(sx - bx) + abs(sy - by)) for sx, sy, bx, by in puzzle]
  ranges = sorted([(x - d, x + d) for x, y, r in data for d in [r-abs(maxi//2-y)] if d >= 0])
  part1 = max([b for _,b in ranges]) - ranges[0][0]

  a = set(x-y+r+1 for x, y, r in data).intersection(x-y-r-1 for x, y, r in data).pop()
  b = set(x+y+r+1 for x, y, r in data).intersection(x+y-r-1 for x, y, r in data).pop()
  part2 = (a+b)//2*maxi + (b-a)//2

  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag15.txt')))
print(pfc()-start)