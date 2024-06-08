import sys

X = sys.stdin.readline().strip()
N = sys.stdin.readline().strip()
used = 0
for i in range(int(N)):
    used += int(sys.stdin.readline().strip())

print(int(X)*int(N) - used + int(X))