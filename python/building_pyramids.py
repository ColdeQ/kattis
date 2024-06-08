import sys
x = sys.stdin.readline().strip()
x = int(x)
height = 0
blocks = 1

while x - blocks*blocks >= 0:
    x -= blocks*blocks
    height +=1
    blocks += 2

print(height)