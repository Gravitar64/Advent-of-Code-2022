from time import perf_counter as pfc
from itertools import combinations


def read_puzzle(file):
  with open(file) as f:
    return [tuple(map(int, line.split(','))) for line in f.readlines()]


def are_neighbors(a,b):
  return sum(abs(d1-d2) for d1,d2 in zip(a,b)) == 1


def get_neighbors(point, minv, maxv):
  neighbors = set()
  for delta in [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]:
    new_point = tuple([d+offset for d,offset in zip(point,delta)])
    if not all([d >= minv and d <= maxv for d in new_point]): continue
    neighbors.add(new_point)
  return neighbors     


def solve(puzzle):
  part1 = 6 * len(puzzle)
  for a,b in combinations(puzzle, 2):
    if not are_neighbors(a,b): continue
    part1 -= 2

  
  part2 = 0
  puzzle = set(puzzle)
  minv = min(min(point) for point in puzzle) -1
  maxv = max(max(point) for point in puzzle) +1
  nodes = [(minv, minv, minv)]
  visited = {nodes[0]}
  while nodes:
    node = nodes.pop()
    for neighbor in get_neighbors(node, minv, maxv):
      if neighbor in visited: continue
      if neighbor in puzzle: 
        part2 += 1
      else:
        visited.add(neighbor)
        nodes.append(neighbor)  

  return part1, part2


time_start = pfc()
print(solve(read_puzzle('Tag18.txt')))
print(pfc()-time_start)