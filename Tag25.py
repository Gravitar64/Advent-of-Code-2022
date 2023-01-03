import time
from functools import reduce
from itertools import zip_longest


def read_puzzle(file):
  with open(file) as f:
    return [line.strip() for line in f.readlines()]


def add_snafu(a,b):
  result, carry = '', 0
  for char1, char2 in zip_longest(a[::-1], b[::-1], fillvalue='0'):
    n1, n2 = s2i[char1], s2i[char2]
    e = carry + n1 + n2
    carry = -1 if e < -2 else 1 if e > 2 else 0
    result += i2s[e - 5 * carry]
  return result[::-1]  
    

def solve(puzzle):
  return reduce(add_snafu,puzzle)


s2i = {'0':0, '1':1, '2':2, '=':-2, '-':-1}
i2s = {v:k for k,v in s2i.items()}

time_start = time.perf_counter()
print(solve(read_puzzle('Tag25.txt')))
print(time.perf_counter()-time_start)