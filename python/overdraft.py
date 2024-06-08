import sys
import math
x = sys.stdin.readline().strip()
x = int(x)
sum = 0
balance = 0
for i in range (x):
    input = sys.stdin.readline().strip()
    num = int(input)
    balance += num

    if balance < 0 and sum < (balance * -1):
        sum = balance * -1



print(int(sum))