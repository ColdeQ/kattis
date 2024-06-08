import sys

A, B, C =sys.stdin.readline().strip().split()
A = int(A)
B = int(B)
C = int(C)
playground = [A, B, C]
jumps =0

while(playground[2] - playground[0] > 2):
    if((playground[1] - playground[0]) < (playground[2] - playground[1])):
        playground[0] = playground[1]
        playground[1] += 1
    else:
        playground[2] = playground[1]
        playground[1] -= 1
    print(playground)

    jumps += 1
print(jumps)