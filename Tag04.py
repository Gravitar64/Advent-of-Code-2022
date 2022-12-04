from time import perf_counter as pfc
import re

def read_puzzle(file):
  with open(file) as f:
    return [map(int,re.findall(r'\d+',line)) for line in f.readlines()]


def solve(puzzle):
  results = [(a <= c and b >=d or c <= a and d >=b, max(a,c) <= min(b,d)) for a,b,c,d in puzzle]
  return list(map(sum, zip(*results)))

start = pfc()
print(solve(read_puzzle('Tag04.txt')))
print(pfc()-start)