from time import perf_counter as pfc


class Node:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.size = 0
    self.childs = []


def read_puzzle(file):
  with open(file) as f:
    return [line.strip() for line in f.readlines()]


def sum_tree(nodes, node):
  if not node.childs:
    return node.size
  for child in node.childs:
    node.size += sum_tree(nodes, nodes[child])
  return node.size


def solve(puzzle):
  root = node = Node(' ', ' ')
  nodes = {' ': root}
  for line in puzzle[1:]:
    if line[0].isdigit():
      node.size += int(line.split()[0])
    elif line.startswith('$ cd '):
      dir_name = line[5:]
      if dir_name == '..':
        node = nodes[node.parent]
      else:
        child = node.name+'/'+dir_name
        node.childs.append(child)
        if child in nodes:
          node = nodes[child]
        else:
          node = Node(child, node.name)
          nodes[child] = node

  sum_tree(nodes, root)

  part1 = sum([node.size for node in nodes.values() if node.size <= 100_000])

  free = 30_000_000 - (70_000_000 - root.size)
  part2 = sorted([node.size for node in nodes.values() if node.size >= free])[0]

  return part1, part2


start = pfc()
print(solve(read_puzzle('Tag07.txt')))
print(pfc()-start)
