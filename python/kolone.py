line = input()
left = input()
right = input()
time = int(input())

arr = []
for i in range(len(left)):
    arr.append([1, left[-1 -i]])

for i in range(len(right)):
    arr.append([2, right[i]])

#print("t = ", 0, arr)
t = 1
while(t <= time and time != 0):
    counter = 0
    while(counter < len(arr) - 1):
        if(arr[counter][0] == 1 and arr[counter+1][0] == 2):
            temp = arr[counter]
            arr[counter] = arr[counter +1]
            arr[counter + 1] = temp
            counter += 2
        else:
            counter += 1
    #print("t = ", t, arr)
    t+=1
    
    

for i in range(len(arr)):
    print(arr[i][1], end='')