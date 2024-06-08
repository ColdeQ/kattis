import sys
N = sys.stdin.readline().strip()
sum = 0.0
for i in range(int(N)):
    a,b = sys.stdin.readline().strip().split(" ")
    sum += float(a) * float(b)
print(sum)