from time import perf_counter as pfc
from pygame import Vector2 as V


def read_puzzle(file):
  with open(file) as f:
    return [line.strip().split() for line in f.readlines()]


def move(rope):
  for i in range(len(rope)-1):
    s1, s2 = rope[i], rope[i+1]
    if s1.distance_to(s2) >= 2:
      dx, dy = s1 - s2
      if abs(dx) > 1:  dx //= abs(dx)
      if abs(dy) > 1:  dy //= abs(dy)
      rope[i+1] = s2 + V(dx, dy)
  return rope


def solve(puzzle, rope_length):
  DIR = dict(R=V(1, 0), L=V(-1, 0), U=V(0, -1), D=V(0, 1))
  rope, tail_trail = [V(0, 0)]*rope_length, set()
  for dir, steps in puzzle:
    for _ in range(int(steps)):
      rope[0] = rope[0] + DIR[dir]
      rope = move(rope)
      tail_trail.add(tuple(rope[-1]))
  return len(tail_trail)


start = pfc()
puzzle = read_puzzle('Tag09.txt')
print(solve(puzzle, 2))
print(solve(puzzle, 10))
print(pfc()-start)