import time


def read_puzzle(file):
  with open(file) as f:
    return [int(n) for n in f.readlines()]


def mix(puzzle, rounds=1):
  indices = list(range(len(puzzle)))
  for i in indices * rounds:
    indices.pop(j := indices.index(i))
    indices.insert((j+puzzle[i]) % len(indices), i)
  zero = indices.index(puzzle.index(0))
  return sum(puzzle[indices[(zero+n) % len(puzzle)]] for n in range(1000, 3001, 1000))


def solve(puzzle):
  part1 = mix(puzzle)
  
  puzzle = [n * 811589153 for n in puzzle]
  part2 = mix(puzzle, rounds=10)
  
  return part1, part2


time_start = time.perf_counter()
print(solve(read_puzzle('Tag20.txt')))
print(time.perf_counter()-time_start)
