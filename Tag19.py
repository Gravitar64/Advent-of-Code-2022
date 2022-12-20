#based on the great work of Dutchcheesehead on reddit (https://www.reddit.com/user/Dutchcheesehead/)

from time import perf_counter as pfc
import re
import math


def read_puzzle(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', line))) for line in f.readlines()]


def quality_heuristic(state):
  mined = state[3]
  return 1000*mined[3] + 100*mined[2] + 10*mined[1] + mined[0]


def bfs(bp, robots, max_minutes, max_queue=1_000):
  _,a,b,c,d,e,f = bp
  costs = [(a, 0, 0, 0), (b, 0, 0, 0),(c, d, 0, 0), (e, 0, f, 0)]
  
  # (minutes, robots, inventory, mined)
  queue = [(0, robots, (0, 0, 0, 0), (0, 0, 0, 0))]
  max_geodes_mined = depth = 0
  
  while queue:
    minutes, robots, inventory, mined = queue.pop(0)

    if minutes > depth:
      queue = sorted(queue, key=quality_heuristic, reverse=True)[:max_queue]
      depth = minutes

    if minutes == max_minutes:
      max_geodes_mined = max(max_geodes_mined, mined[3])
      continue

    # Mine material with the robots (0 = ores ... 3 = geodes)
    new_inventory = [inventory[i] + robots[i] for i in range(4)]
    new_mined = [mined[i] + robots[i] for i in range(4)]

    # Case of not building a robot
    queue.append((minutes+1, robots, new_inventory, new_mined))

    # Build new robots, and try building each type of robot
    for i in range(4):
      cost_robot = costs[i]

      # Check if we have enough materials to build a robot
      if all([inventory[j] >= cost_robot[j] for j in range(4)]):  #
        new_robots = list(robots)
        new_robots[i] += 1
        new_inventory_state = [new_inventory[j] - cost_robot[j] for j in range(4)]
        queue.append((minutes+1, new_robots, new_inventory_state, new_mined))
  return max_geodes_mined


def solve(puzzle):
  robots = (1, 0, 0, 0)
  part1 = sum(bp[0] * bfs(bp, robots, 24) for bp in puzzle)
  part2 = math.prod(bfs(bp, robots, 32) for bp in puzzle[:3])
  return part1, part2


time_start = pfc()
print(solve(read_puzzle('Tag19.txt')))
print(pfc()-time_start)
