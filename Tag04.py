from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [line.strip() for line in f.readlines()]


def get_sets(line):
  pairs = [map(int,pair.split('-')) for pair in line.split(',')]
  return [set(range(f,t+1)) for f,t in pairs]
  

def solve(puzzle):
  sum1 = sum2 = 0
  for line in puzzle:
    a, b = get_sets(line)
    if a.issubset(b) or b.issubset(a): sum1 += 1
    if set.intersection(a, b):         sum2 += 1
  return sum1, sum2


start = pfc()
print(solve(read_puzzle('Tag04.txt')))
print(pfc()-start)