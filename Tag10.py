from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [line.strip().split() for line in f.readlines()]


def solve(puzzle):
  part1, cycles, x = 0, [1,1], 1
  for line in puzzle:
    if line[0] == 'noop':
      cycles.append(x)
    else:
      cycles.append(x)
      x += int(line[1])
      cycles.append(x)
  
  part2 = []
  for c in range(241):
    if not c % 40: part2.append('\n')
    part2.append('█' if c % 40 - cycles[c+1] in {-1,0,1} else ' ')
  print(''.join(part2))
     
  part1 = sum([c*cycles[c] for c in range(20,241,40)])
  return part1

start = pfc()
print(solve(read_puzzle('Tag10.txt')))
print(pfc()-start)
