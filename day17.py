# Advent of Code
# Day 17

containerList = '''11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3
'''

class Container(object):
    def __init__(self, capacity):
        self.capacity = capacity
        
def getInventory(capacityList):
    containers = []
    for item in capacityList:
        newContainer = Container(int(item))
        containers.append(newContainer)
        
    return containers

containers = getInventory(containerList.splitlines())

import itertools

target = 150
nFound = 0
minNumberOfContainers = None
comboCount = 0
comboList = []

for nContainers in range(len(containers)):
    for containerSequence in itertools.combinations(containers, nContainers):
        runningTotal = 0
        for container in containerSequence:
            runningTotal += container.capacity
            if runningTotal > target:
                break
            
        if runningTotal == target:
            nFound += 1
            if minNumberOfContainers == None:
                minNumberOfContainers = len(containerSequence)
                comboList.append(containerSequence)
                comboCount += 1
            else:
                if len(containerSequence) == minNumberOfContainers:
                    comboCount += 1
                    comboList.append(containerSequence)
            
print("There are {0:d} combinations of containers to carry {1:d} L of eggnog.".format(nFound, target))
print("The minimum number of containers is {0:d} and that can be achieved {1:d} ways:".format(minNumberOfContainers, comboCount))

for item in comboList:
    print("  {0} = {1:d}".format(' + '.join([str(i.capacity) for i in item]), target))
    