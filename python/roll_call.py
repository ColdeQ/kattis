import sys

sorted_list = []
name_list = []
for line in sys.stdin:

    if len(sorted_list) == 0:
        name = line.strip().split()
        sorted_list.append([name[1], name[0]])
        name_list.append(name[0])
    else:
        name = line.strip().split()
        sorted_list.append([name[1], name[0]])
        sorted_list = sorted(sorted_list)
        name_list.append(name[0])

for i in range(len(sorted_list)):

    name = sorted_list[i]

    if len(sorted_list) == 1:
        print(name[1], name[0])
    elif i == 0:
        if name_list.count(name[1]) == 1:
            print(name[1])
        else:
            print(name[1], name[0])