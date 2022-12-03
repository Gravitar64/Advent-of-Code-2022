from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [rucksack.strip() for rucksack in f.readlines()]


def solve(puzzle):
  f = lambda x: ord(x)-96 if x.islower() else ord(x)-38
  
  sum1, sum2, group = 0, 0, []
  for rucksack in puzzle:
    # part1
    l = len(rucksack)
    compartments = [set(rucksack[:l//2]), set(rucksack[l//2:])]
    sum1 += f(set.intersection(*compartments).pop())
    
    # part2
    if len(group) < 3:
      group.append(set(rucksack))
    if len(group) == 3:
      sum2 += f(set.intersection(*group).pop())
      group = []
  
  return sum1, sum2  


start = pfc()
print(solve(read_puzzle('Tag03.txt')))
print(pfc()-start)
