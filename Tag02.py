from time import perf_counter as pfc


def read_puzzle(file):
  with open(file) as f:
    puzzle = [zeile.split() for zeile in f.readlines()]
    return [(ord(a)-64, ord(b)-87) for a,b in puzzle]


def solve(puzzle):
  ROCK, PAPER, SCISSOR = 1,2,3
  WIN, DRAW = 6, 3
  winner = {ROCK:PAPER, PAPER:SCISSOR, SCISSOR:ROCK}
  looser = {b:a for a,b in winner.items()}
  score1 = score2 = 0
  for a,b in puzzle:
    score1 += b + DRAW if a == b else b + WIN if winner[a] == b else b
    score2 += a + DRAW if b == 2 else winner[a] + WIN if b == 3 else looser[a]
  return score1, score2


start = pfc()
print(solve(read_puzzle('Tag02.txt')))
print(pfc()-start)