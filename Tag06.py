from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return f.read()


def solve(puzzle, l):
  for i in range(0, len(puzzle)-l):
    if len(set(puzzle[i:i+l])) == l:
      return i+l


start = pfc()
puzzle = read_puzzle('Tag06.txt')
print(solve(puzzle, 4))
print(solve(puzzle, 14))
print(pfc()-start)
