from time import perf_counter as pfc
from itertools import product


def read_puzzle(file):
  with open(file) as f:
    return [line.strip().split() for line in f.readlines()]


def tail_follow(tail,head_trail,part1):
  tx,ty = tail
  if part1: 
    hx,hy = head_trail[-1]
  elif len(head_trail)>9:
    hx,hy = head_trail[-10]
  else:
    return (tx,ty)
  touching = set([(hx+dx, hy+dy) for dx,dy in product((-1,0,1),repeat=2)])
  if tail in touching: return tail
  dx,dy = hx-tx, hy-ty
  if abs(dx) > 1: dx //= abs(dx)
  if abs(dy) > 1: dy //= abs(dy)

  return (tx+dx, ty+dy)



def solve(puzzle,part1):
  DIR = dict(R=(1,0), U=(0,-1), D=(0,1), L=(-1,0))
  tail_trail, head_trail = [(0,0)], [(0,0)]
  tail, head = (0,0), (0,0)
  for dir, steps in puzzle:
    steps = int(steps)
    dx,dy = DIR[dir]
    for mul in range(1,steps+1):
      x,y = head
      nx, ny = x+dx*mul, y+dy*mul
      if part1:
        head_trail.append((nx,ny))
      elif (nx,ny) not in head_trail:
        head_trail.append((nx,ny))
      tail = tail_follow(tail, head_trail, part1)
      tail_trail.append(tail)
    head = (nx,ny)  
  for a,b in zip(head_trail, tail_trail):
    print(a,b)
  
  return len(set(tail_trail))      
      


start = pfc()
puzzle = read_puzzle('Tag09.txt')
#print(solve(puzzle, True))
print(solve(puzzle, False))
print(pfc()-start)