from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return {(x, y): ord(e)-96 if e.islower() else e
            for y, line in enumerate(f.readlines())
            for x, e in enumerate(line.strip())}


def neighbors(puzzle, x, y):
  for new in [(x+dx, y+dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
    if puzzle.get(new, 100) - puzzle[(x, y)] > 1: continue
    yield new


def find_shortest_path(puzzle, start, end):
  paths, visited, path_index = [[start]], {start}, 0

  while path_index < len(paths):
    actual_path = paths[path_index]
    last_pos = actual_path[-1]
    for neighb in neighbors(puzzle, *last_pos):
      if neighb in visited: continue
      if neighb == end: return len(actual_path)
      paths.append((actual_path.copy() + [neighb]))
      visited.add(neighb)
    path_index += 1

  return 999999


def solve(puzzle):
  start_pos = []

  for pos, value in puzzle.items():
    if value == 'S':
      start = pos
      puzzle[start] = 1
    if value == 'E':
      end = pos
      puzzle[end] = 26
    if puzzle[pos] == 1:
      start_pos.append(pos)

  part1 = find_shortest_path(puzzle, start, end)
  part2 = min([find_shortest_path(puzzle, start, end) for start in start_pos])

  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag12.txt')))
print(pfc()-start)
