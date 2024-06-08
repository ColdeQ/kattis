rods = input()
sum = 0
for i in range(int(rods)):
    line = input().strip()
    sum += int(line)
print(sum - int(rods) + 1)