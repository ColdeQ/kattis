import sys
length = sys.stdin.readline().strip()
line = sys.stdin.readline()
saved = []
fault = 0
for i in range(int(length)):
    if line[i] == '(' or line[i] == '[' or line[i] == '{':
        saved.append(line[i])

    elif line[i] == ')':
        if len(saved) > 0:
            if saved[-1] == '(':
                saved.pop(len(saved)-1)
            else:
                print(line[i], i)
                fault = 1
                break
        else:
            print(line[i], i)
            fault = 1
            break   

    elif line[i] == ']':
        if len(saved) > 0:
            if saved[-1] == '[':
                saved.pop(len(saved)-1)
            else:
                print(line[i], i)
                fault = 1
                break
        else:
            print(line[i], i)
            fault = 1
            break

    elif line[i] == '}':
        if len(saved) > 0:
            if saved[-1] == '{':
                saved.pop(len(saved)-1)
            else:
                print(line[i], i)
                fault = 1
                break
        else:
            print(line[i], i)
            fault = 1
            break

if fault == 0:
    print("ok so far")