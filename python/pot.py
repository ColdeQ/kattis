import sys
import math
x = sys.stdin.readline().strip()
x = int(x)
sum = 0
for i in range (x):
    input = sys.stdin.readline().strip()
    num = int(input[:-1])
    pow = int(input[-1])
    sum += math.pow(num,pow)

print(int(sum))