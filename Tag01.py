from time import perf_counter as pfc

def read_puzzle(file):
  with open(file) as f:
    return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]


def solve(puzzle):
  puzzle = sorted(puzzle, reverse=True)
  return puzzle[0], sum(puzzle[:3])


start=pfc()
print(solve(read_puzzle('Tag01.txt')))
print(pfc()-start)