from time import perf_counter as pfc
from functools import cmp_to_key


def read_puzzle(file):
  with open(file) as f:
    return [eval(line.strip()) for line in f.readlines() if line > ' ']


def correct_order(left, right):
  if type(left) is list or type(right) is list:
    if type(left)  is not list: left  = [left]
    if type(right) is not list: right = [right]
    for l,r in zip(left,right):
      c = correct_order(l,r)
      if c != 0: return c
    return len(left) - len(right)
  else:
    return left - right    



def solve(puzzle):
  part1 = 0
  for i,(left,right) in enumerate(zip(puzzle[::2], puzzle[1::2]),1):
    if correct_order(left, right) >= 0: continue
    part1 += i
  
  puzzle += [[[2]], [[6]]]
  puzzle = sorted(puzzle, key=cmp_to_key(correct_order))
  part2 = (puzzle.index([[2]])+1) *  (puzzle.index([[6]])+1)
  
  
  return part1, part2
  
  
start = pfc()
print(solve(read_puzzle('Tag13.txt')))
print(pfc()-start)