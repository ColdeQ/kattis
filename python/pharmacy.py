from queue import PriorityQueue
import sys

remoteQueue = PriorityQueue()
storeQueue = PriorityQueue()

precsriptions, technicians  = sys.stdin.readline().strip().split(" ")

totalStore = 0
totalRemote = 0
for i in range(int(precsriptions)):
    time, dropType, timeToProcess = sys.stdin.readline().strip().split(" ")
    if dropType == 'R':
        remoteQueue.put((int(time), int(1), int(timeToProcess)))
        totalRemote +=1
    else:
        storeQueue.put((int(time), int(0), int(timeToProcess)))
        totalStore += 1

timer = 1
workerArray = []
totalStoreTime = 0
totalRemoteTime = 0
completedPerscriptions = 0

def prioSort(x):
    return x[0]
    
while(precsriptions != completedPerscriptions):

    if(len(workerArray) > 0):
        while workerArray[0][0] == timer:
            order = workerArray.pop(0)
            if order[2] == 1:
                totalRemoteTime += (timer - order[1])
            else:
                totalStoreTime += (timer - order[1])
            completedPerscriptions+=1
            if(len(workerArray) == 0):
                break

    while(len(workerArray) < int(technicians)):
        if (storeQueue.qsize() != 0) and (storeQueue.queue[0][0] <= timer):
            dequed = storeQueue.get(0)
            workerArray.append((int(timer+dequed[2]), int(dequed[0]),int( dequed[1])))
            workerArray.sort(key=prioSort)
        elif((remoteQueue.qsize() != 0 ) and (remoteQueue.queue[0][0] <= timer)):
            dequed = remoteQueue.get(0)
            workerArray.append((int(timer+dequed[2]), int(dequed[0]),int( dequed[1])))
            workerArray.sort(key=prioSort)
        else:
            break
    timer+=1

if totalStore == 0 and totalRemote == 0:
    print(0 ,0)
elif totalStore == 0:
    print(0,float(totalRemoteTime/totalRemote))
elif totalRemote == 0:
    print(float(totalStoreTime/totalStore),0)
else:
    print(float(totalStoreTime/totalStore), float(totalRemoteTime/totalRemote))