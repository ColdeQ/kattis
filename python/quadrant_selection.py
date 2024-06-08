import sys
x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
x = int(x)
y = int(y)
print(1) if (x > 0 and y > 0) else print(4) if(x > 0 and y < 0) else print(2) if (x < 0 and y > 0) else print(3)