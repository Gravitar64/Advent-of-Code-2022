from time import perf_counter as pfc
import re
from collections import defaultdict


def read_puzzle(file):
  with open(file) as f:
    return f.readlines()


def rearrange(s, a, f, t, part1):
  move = s[f][:a][::-1] if part1 else s[f][:a]
  s[t] = move + s[t]
  s[f] = s[f][a:]


def get_first_crates(stacks):
  return ''.join([v[0] for _, v in sorted(stacks.items())])


def solve(puzzle):
  instructions, stacks1 = [], defaultdict(str)
  for line in puzzle:
    if line[0] == 'm':
      instructions.append(list(map(int, re.findall('\d+', line))))
    else:
      for i, char in enumerate(line):
        if not char.isalpha():
          continue
        stacks1[i//4+1] += char

  stacks2 = stacks1.copy()
  for a, f, t in instructions:
    rearrange(stacks1, a, f, t, True)
    rearrange(stacks2, a, f, t, False)

  return get_first_crates(stacks1), get_first_crates(stacks2)


start = pfc()
print(solve(read_puzzle('Tag05.txt')))
print(pfc()-start)
