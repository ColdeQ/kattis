    import sys
    x = sys.stdin.readline().strip()
    for i in range(1,int(x)+1):
        toPrint = sys.stdin.readline().strip()
        if i % 2 != 0:
            print(toPrint)