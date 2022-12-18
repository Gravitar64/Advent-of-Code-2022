from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [ord(e)-61 for e in f.read().strip()]


def gültig(rock):
  return all([-1 < x < 7 and y > 0 for x, y in rock])


def search_intervall(cache, key, rock_nr, height):
  if key in cache:
    last_rock_nr, last_height = cache[key]
    rocks_to_go = 1e12-rock_nr
    intervall_rocks = rock_nr - last_rock_nr
    intervall_height = height - last_height
    quotient, remainder = divmod(rocks_to_go, intervall_rocks)
    if not remainder:
      return int(height + intervall_height * quotient)
  else:
    cache[key] = rock_nr, height


def solve(jets):
  tower, cache, tower_height, rock_i, jet_i = set(), dict(), 0, 0, 0
  rocks = [[(0, 0), (1, 0), (2, 0), (3, 0)],
           [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
           [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
           [(0, 0), (0, 1), (0, 2), (0, 3)],
           [(0, 0), (1, 0), (0, 1), (1, 1)]]
  rock_height = [1, 3, 3, 4, 2]

  for rock_nr in range(int(1e12)):
    
    if rock_nr == 2022: part1 = tower_height
    if (part2 := search_intervall(cache,(rock_i, jet_i),rock_nr,tower_height)):
      return part1, part2
 
    x, y = 2, tower_height+3+rock_height[rock_i]
    rock = rocks[rock_i]

    while True:
      new_x = x+jets[jet_i]
      jet_i = (jet_i+1) % len(jets)
      
      #left/right
      rock_pos = set([(new_x+dx, y-dy) for dx, dy in rock])
      if not rock_pos & tower and gültig(rock_pos):
        x = new_x
      
      #down
      rock_pos = set([(x+dx, y-dy-1) for dx, dy in rock])
      if not rock_pos & tower and gültig(rock_pos):
        y -= 1
      else:
        break

    tower |= set([(x+dx, y-dy) for dx, dy in rock])
    tower_height = max(tower_height, y)
    rock_i = (rock_i+1) % len(rocks)


time_start = pfc()
print(solve(read_puzzle('Tag17.txt')))
print(pfc()-time_start)