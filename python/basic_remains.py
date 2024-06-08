import sys
import math

def toDeci(number, base):
    sum = 0
    for i in range(len(number)):
        sum += int(number[-1 - i ]) * math.pow(int(base),i)
    return sum    

def toBase(number, base):
    sum = []
    while(number >= int(base)):
        sum.append(int(number % int(base)))
        number = int(number / int(base))
    if(number > 0):
        sum.append(int(number))
    return sum

line  = input()
res = []
while(line[0] != '0'):
    base, number, divisor = line.strip().split(" ")
    if(not(int(base) == 10)):
        deci = toDeci(number, base)
        devisorDeci = toDeci(divisor, base)
        rest = deci % devisorDeci
        res.append(toBase(rest, base))
    else:
        res.append([int(int(number) % int(divisor))])
    line = input()


def printArray(arrays):
    for i in range(len(arrays)):
        print(arrays[-1 - i], end='')

for i in range(len(res)):
    printArray(res[i])
    if not (i == (len(res)-1)):
        print()