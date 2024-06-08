import sys
a,b = sys.stdin.readline().strip().split(" ")
print(a, b) if int(a) < int(b) else print(b,a)