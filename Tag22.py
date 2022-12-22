import time
import re

side_switch = {(1,0,-1):lambda y,x: (149-y,0),
               (1,-1,0):lambda y,x: (x-50+150,0),
               (2,0,1):lambda y,x: (149-y,99),
               (2,-1,0):lambda y,x: (199,x-100),
               (2,1,0):lambda y,x: (x-100+50,99),
               (4,0,1):lambda y,x: (49,y-50+100),
               (4,0,-1): lambda y,x: (100,y-50),
               (7,0,1):lambda y,x: (49-(y-100),149),
               (7,1,0): lambda y,x: (150+(x-50),49),
               (6,-1,0): lambda y,x: (x+50,50),
               (6,0,-1): lambda y,x: (49-(y-100),50),
               (9,0,-1): lambda y,x: (0,y-150+50),
               (9,0,1): lambda y,x: (149,(y-150)+50),
               (9,1,0): lambda y,x: (0,x+100)}
dir_switch = {(1,0,-1):(0,1),
              (1,-1,0):(0,1),
              (2,0,1): (0,-1),
              (2,-1,0): (-1,0),
              (2,1,0) : (0,-1),
              (4,0,1): (-1,0),
              (4,0,-1): (1,0), 
              (7,0,1) :(0,-1),
              (7,1,0): (0,-1),
              (6,-1,0): (0,1),
              (6,0,-1): (0,1),
              (9,0,-1): (1,0),
              (9,0,1): (-1,0),
              (9,1,0): (1,0)
              }


def read_puzzle(file):
  with open(file) as f:
    return [[char for char in line] for line in f.read().split('\n')]


def wrap_around(grid,pos,dir,part1):
  (y,x), (dy,dx) = pos, dir
  if part1:
    if dx == 1: x = min([gx for gy,gx in grid if gy == y])
    if dx == -1: x = max([gx for gy,gx in grid if gy == y])
    if dy == 1: y = min([gy for gy,gx in grid if gx == x])
    if dy == -1: y = max([gy for gy,gx in grid if gx == x])
    if grid[(y,x)] == '.': return (y,x), dir
  else:
    side = y // 50 * 3 + x // 50
    pos = side_switch[(side,dy,dx)](y,x)
    dir = dir_switch[(side,dy,dx)]
    if grid[pos] == '.': return pos, dir

  
def move_rotate(grid, pos, dir, route, part1):
  (y,x), (dy,dx) = pos, dir
  if route.isdigit():
    for _ in range(int(route)):
      yn, xn = y+dy, x+dx
      if (v:=grid.get((yn,xn),' ')) == '.':
        y,x = yn, xn
      elif v == '#':
        return (y,x), (dy,dx)
      else:
        if not (v := wrap_around(grid,(y,x),(dy,dx),part1)): return (y,x), (dy,dx)
        (y,x), (dy,dx) = v
    return (y,x), (dy,dx)
  else:
    dir = (dx,-dy) if route == 'R' else (-dx,dy)
    return pos, dir


def solve(puzzle,part1=True):
  route = re.findall('\d+|R|L', ''.join(puzzle[-1]))
  grid = {(y,x):char for y,line in enumerate(puzzle[:-2]) for x,char in enumerate(line) if char != ' '}
  dir = (0,1) #(y,x-format)
  pos = min(grid)
  for r in route:
    pos, dir = move_rotate(grid, pos, dir, r, part1)
  row, col = pos
  facing = [(0,1), (1,0), (0,-1), (-1,0)].index(dir)
  return 1000 * (row+1) + 4 * (col+1) + facing

  
time_start = time.perf_counter()
print(solve(read_puzzle('Tag22.txt')))
print(solve(read_puzzle('Tag22.txt'), False))
print(time.perf_counter()-time_start)
