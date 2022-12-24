import time
import sympy


def read_puzzle(file):
  with open(file) as f:
    return [line.strip().replace(':', '=') for line in f.readlines()]


def solve(puzzle, part1=True):
  l = {} 
  if not part1:
    for i, line in enumerate(puzzle):
      if not line.startswith('humn'): continue
      puzzle[i] = 'humn = sympy.Symbol("x")'
  
  while 'root' not in l:
    for line in puzzle:
      try:
        exec(line, None, l)
      except:
        pass
  
  return l['root'] if part1 else sympy.solve(l['pdzb'] - l['bhlw'], sympy.Symbol('x'))     
  

time_start = time.perf_counter()
print(solve(read_puzzle('Tag21.txt')))
print(solve(read_puzzle('Tag21.txt'), False))
print(time.perf_counter()-time_start)
