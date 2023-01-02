import time


def read_puzzle(file):
  walls, blizzards, empties = set(), set(), []
  with open(file) as f:
    for y, line in enumerate(f.readlines()):
      for x, char in enumerate(line.strip()):
        if char == '#':       walls.add((x-1, y-1))
        if char in DIRS:      blizzards.add((x-1, y-1, *DIRS[char]))
        if char == '.':       empties.append((x-1, y-1))
  return walls, blizzards, empties


def bfs(blizzards, walls, entry, target, width, height, t=0):
  waypoints, q, results = [target, entry, target], {entry}, []

  while waypoints:
    t += 1
    move_to = {(x+dx, y+dy) for x, y in q for dx, dy in MOVES}
    blizzs = {((x+dx*t) % width, (y+dy*t) % height) for x, y, dx, dy in blizzards}
    q = move_to - blizzs - walls
    if waypoints[0] in q:
      results.append(t)
      q = {waypoints.pop(0)}
  return results


def solve(walls, blizzards, empties):
  entry, target = empties[0], empties[-1]
  width, height = target[0]+1, target[1]
  walls |= {(entry[0], entry[1]-1), (target[0], target[1]+1)}
  part1 = bfs(blizzards, walls, entry, target, width, height)
  return part1


DIRS = {'v': (0, 1), '<': (-1, 0), '>': (1, 0), '^': (0, -1)}
MOVES = list(DIRS.values()) + [(0, 0)]

time_start = time.perf_counter()
print(solve(*read_puzzle('Tag24.txt')))
print(time.perf_counter()-time_start)
