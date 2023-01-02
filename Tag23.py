import time
import itertools
import collections


def read_puzzle(file):
  with open(file) as f:
    return {complex(x, y) for y, line in enumerate(f.readlines()) for x, char in enumerate(line) if char == '#'}


def any_neighbors(pos, puzzle):
  return any((pos+delta) in puzzle for delta in neighbors)


def possible_destinations(poss_mover, moving_order, puzzle):
  poss_dest = collections.defaultdict(list)
  for pos in poss_mover:
    for dir in moving_order:
      if any(pos+delta in puzzle for delta in move_dir[dir]): continue
      poss_dest[pos + move_dir[dir][1]].append(pos)
      break
  return poss_dest


def solve(puzzle):
  moving_order = 'NSWE'
  for round in range(1, 1000):
    no_mover = {pos for pos in puzzle if not any_neighbors(pos, puzzle)}
    poss_mover = puzzle - no_mover
    poss_dest = possible_destinations(poss_mover, moving_order, puzzle)
    destinations = {key: val[0] for key, val in poss_dest.items() if len(val) == 1}
    puzzle = puzzle - set(destinations.values()) | set(destinations.keys())
    moving_order = moving_order[1:]+moving_order[0]

    if round == 10:
      xs, ys = [int(x.real) for x in puzzle], [int(x.imag) for x in puzzle]
      part1 = (max(xs) - min(xs)+1) * (max(ys) - min(ys)+1) - len(puzzle)

    if not destinations:
      part2 = round
      break

  return part1, part2


neighbors = [complex(x, y) for x, y in itertools.product( [-1, 0, 1], repeat=2) if (x, y) != (0, 0)]
move_dir = dict(N=[-1-1j, 0-1j, 1-1j],
                S=[-1+1j, 0+1j, 1+1j],
                W=[-1-1j, -1+0j, -1+1j],
                E=[1-1j, 1+0j, 1+1j])

time_start = time.perf_counter()
print(solve(read_puzzle('Tag23.txt')))
print(time.perf_counter()-time_start)