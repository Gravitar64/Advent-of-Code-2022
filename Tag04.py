from time import perf_counter as pfc
import re


def read_puzzle(file):
  with open(file) as f:
    return [list(map(int,re.findall('\d+',line))) for line in f.readlines()]


def solve(puzzle):
  sum1 = sum([a <= c and b >= d or c <= a and d >= b for a,b,c,d in puzzle])
  sum2 = sum([max(a,c) <= min(b,d) for a,b,c,d in puzzle])
  return sum1, sum2

start = pfc()
print(solve(read_puzzle('Tag04.txt')))
print(pfc()-start)