import re
import time
import itertools


def read_puzzle(file):
  with open(file) as f:
    return [re.findall('[A-Z]+|\d+', line[1:]) for line in f.readlines()]


def solve(puzzle):
  graph = {valve:leads for valve, _, *leads in puzzle}
  flows = {valve: int(flow) for valve, flow, *_ in puzzle if flow != '0'}
  indicies = {valve: 1 << i for i, valve in enumerate(flows)}
  distances = {(v,l): 1 if l in graph[v] else 1000 for l in graph for v in graph}

  # floyd-warshall = Distance for any possible pair of valves
  for k, i, j in itertools.product(graph, graph, graph):
    distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])


  def visit(valve, time, bitmask, pressure, answer):
    answer[bitmask] = max(answer.get(bitmask, 0), pressure)
    for no_empty in flows:
      rem_time = time - distances[valve, no_empty] - 1
      if indicies[no_empty] & bitmask or rem_time <= 0: continue
      visit(no_empty, rem_time, bitmask|indicies[no_empty], pressure + flows[no_empty] * rem_time, answer)
    return answer


  part1     = max(visit('AA', 30, 0, 0, {}).values())
  visited2  = visit('AA', 26, 0, 0, {})
  part2     = max(v1+v2 for bitm1, v1 in visited2.items()
                  for bitm2, v2 in visited2.items() if not bitm1 & bitm2)
  
  return part1, part2


time_start = time.perf_counter()
print(solve(read_puzzle('Tag16.txt')))
print(time.perf_counter()-time_start)