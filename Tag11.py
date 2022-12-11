from time import perf_counter as pfc
import re
import math


class Monkey:
  def __init__(self, items, op, divisor, dest):
    self.items = items
    self.op = op
    self.divisor = divisor
    self.dest = dest
    self.act = 0

  def inspection(self, part1):
    for item in self.items:
      op, value = self.op
      value = item if value == 'old' else int(value)
      item = item * value if op == '*' else item + value
      item = item // 3 if part1 else item % magic_divisor
      monkeys[self.dest[bool(item % self.divisor)]].items.append(item)
      self.act += 1
    self.items = []


def read_puzzle(file):
  with open(file) as f:
    return [[l for l in m.split('\n')] for m in f.read().split('\n\n')]


def solve(puzzle, part1):
  for monkey in puzzle:
    items = list(map(int, re.findall('\d+', monkey[1])))
    op = monkey[2][23:].split()
    divisor = int(monkey[3][21:])
    dest = [int(monkey[4][29]), int(monkey[5][30])]
    monkeys.append(Monkey(items, op, divisor, dest))

  rounds = 20 if part1 else 10_000
  for _ in range(rounds):
    for monkey in monkeys:
      monkey.inspection(part1)

  return math.prod(sorted([m.act for m in monkeys])[-2:])


start = pfc()
monkeys = []
print(solve(read_puzzle('Tag11.txt'), True))
magic_divisor = math.prod([m.divisor for m in monkeys])
monkeys = []
print(solve(read_puzzle('Tag11.txt'), False))
print(pfc()-start)
