from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    return [list(map(int, line.strip()))for line in f.readlines()]


def visibility_score(row, col):
  h, w = len(puzzle), len(puzzle[0])
  is_visible, score = False, 1
  for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
    shorter = True
    for mul in range(1, max(h, w)+1):
      nrow, ncol = row+dr*mul, col+dc*mul
      if nrow < 0 or nrow >= h or ncol < 0 or ncol >= w:
        score *= mul-1
        break
      if puzzle[nrow][ncol] >= puzzle[row][col]:
        shorter = False
        score *= mul
        break
    if shorter:
      is_visible = True
  return is_visible, score


def solve(puzzle):
  trees = max_score = 0
  for row in range(len(puzzle)):
    for col in range(len(puzzle[0])):
      is_visible, score = visibility_score(row, col)
      if is_visible:
        trees += 1
      max_score = max(max_score, score)
  return trees, max_score


start = pfc()
puzzle = read_puzzle('Tag08.txt')
print(solve(puzzle))
print(pfc()-start)