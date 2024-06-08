import sys

floors, start, goal, up, down = sys.stdin.readline().strip().split()


class node:
  def __init__(self, floor, goUp,goDown,depth):
    self.floor = floor
    self.goUp = goUp
    self.goDown = goDown
    self.depth = depth

node = node(int(start), int(start) + int(up), int(start) - int(down), 0)

visitedFloors = []
queue = []

queue.append(node)
visitedFloors.append(node)

depth = 1

while(len(queue) != 0):




    depth+=1