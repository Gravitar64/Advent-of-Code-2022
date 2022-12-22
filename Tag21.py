import time
import sympy


def read_puzzle(file):
  with open(file) as f:
    return [line.strip() for line in f.readlines()]


def get_monkey(monkeys, name):
  if isinstance(monkeys[name], sympy.Symbol): return monkeys[name]
  elif monkeys[name].isdigit():               return int(monkeys[name])
  else:
    left, op, right = monkeys[name].split()
    return eval(f"get_monkey(monkeys, left) {op} get_monkey(monkeys, right)")


def solve(puzzle):
  monkeys = dict(line.split(': ') for line in puzzle)
  part1 = int(get_monkey(monkeys, "root"))

  monkeys['humn'] = sympy.Symbol('x')
  left, _, right = monkeys['root'].split()
  print(get_monkey(monkeys, left))
  print(get_monkey(monkeys, right))

  part2 = sympy.solve(get_monkey(monkeys, left) - get_monkey(monkeys, right),
                      sympy.Symbol('x'))

  return part1, part2


time_start = time.perf_counter()
print(solve(read_puzzle('Tag21.txt')))
print(time.perf_counter()-time_start)
