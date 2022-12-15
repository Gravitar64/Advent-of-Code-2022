from time import perf_counter as pfc
import re


def read_puzzle(file):
  with open(file) as f:
    return [list(map(int, re.findall('\-?\d+', line))) for line in f.readlines()]


def generate_ranges(sensor_dist, target_row):
  ranges = []
  for col, row, dist_beacon in sensor_dist:
    overlap_target_row = dist_beacon - abs(target_row - row)
    if overlap_target_row < 0: continue
    ranges.append([col - overlap_target_row, col + overlap_target_row])

  ranges.sort()
  consolidate = []
  start, end = ranges[0]
  for s, e in ranges[1:]:
    if end >= s:
      end = max(end, e)
    else:
      consolidate.append((start, end))
  if (start, end) not in consolidate:
    consolidate.append((start, end))
  return consolidate


def solve(puzzle):
  sensor_dist = [(sx, sy, abs(sx - bx) + abs(sy - by)) for sx, sy, bx, by in puzzle]
  start, end = generate_ranges(sensor_dist, 2_000_000)[0]
  part1 = end - start

  for row in range(4_000_001):
    ranges = generate_ranges(sensor_dist, row)
    if len(ranges) == 1: continue
    part2 = (ranges[0][1]+1) * 4_000_000 + row
    break

  return part1, part2

  #
start = pfc()
print(solve(read_puzzle('Tag15.txt')))
print(pfc()-start)
