from time import perf_counter as pfc
import re
import math


class Monkey:
  def __init__(self, items, op, amount, divisor, t, f):
    self.items = items
    self.op = op
    self.amount = amount
    self.divisor = divisor
    self.t = t
    self.f = f
    self.act = 0

  def inspections(self, part1):
    for item in self.items:
      if self.amount == 'old':
        item *= item
      elif self.op == '*':
        item *= int(self.amount)
      elif self.op == '+':
        item += int(self.amount)
      if part1:
        item //= 3
      else:
        item %= modulo_trick
      dest = self.f if item % self.divisor else self.t
      monkeys[dest].items.append(item)
      self.act += 1
    self.items = []


def read_puzzle(file):
  with open(file) as f:
    return [[l for l in m.split('\n')] for m in f.read().split('\n\n')]


def solve(puzzle, part1):
  for monkey in puzzle:
    items = list(map(int, re.findall('\d+', monkey[1])))
    op = monkey[2][23]
    amount = monkey[2][25:]
    divisor = int(re.search('\d+', monkey[3]).group())
    t = int(re.search('\d+', monkey[4]).group())
    f = int(re.search('\d+', monkey[5]).group())
    monkeys.append(Monkey(items, op, amount, divisor, t, f))

  rounds = 20 if part1 else 10_000
  for _ in range(rounds):
    for monkey in monkeys:
      monkey.inspections(part1)

  return math.prod(sorted([m.act for m in monkeys], reverse=True)[:2])


start = pfc()
monkeys = []
print(solve(read_puzzle('Tag11.txt'), True))
modulo_trick = math.prod([m.divisor for m in monkeys])
monkeys = []
print(solve(read_puzzle('Tag11.txt'), False))
print(pfc()-start)
