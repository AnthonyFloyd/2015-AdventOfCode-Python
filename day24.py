#
# Advent of code
# Day 24
#
# It Hangs in the Balance
#
import itertools

day24PresentsRaw="""1
3
5
11
13
17
19
23
29
31
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
"""

day24Presents = [int(item) for item in day24PresentsRaw.splitlines()]

global target, allSolutions, lowestQuantumEntanglement, bestSolution

def divideIntoGroups(presentList, nGroups):
    global target, allSolutions, lowestQuantumEntanglement, bestSolution
    
    for groupLength in range(1, len(presentList)):
        for presentGroup in itertools.combinations(presentList, groupLength):
            total = sum(presentGroup)
            if total == target and nGroups == 2:
                set1 = set(day24Presents).difference(set(presentList))
                set2 = set(presentGroup)
                set3 = set(presentList).difference(set2)
                allSolutions.append((set1, set2, set3))
                
                return True
            elif total == target and divideIntoGroups(set(presentList).difference(set(presentGroup)), nGroups - 1):
                QE = 1
                for present in presentGroup:
                    QE *= present
                if lowestQuantumEntanglement is None:
                    bestSolution = allSolutions[-1]
                    lowestQuantumEntanglement = QE
                else:
                    if QE < lowestQuantumEntanglement:
                        bestSolution = allSolutions[-1]
                        lowestQuantumEntanglement = QE
                    
                return True
    return False
            
if __name__ == '__main__':
    global target, allSolutions, lowestQuantumEntanglement, bestSolution

    print("Part 1")
    
    # divide the presents into 3 groups such that each of the 3 groups has equal weights
    
    target = sum(day24Presents) / 3
    allSolutions = []
    lowestQuantumEntanglement = None
    bestSolution = None    
    
    divideIntoGroups(day24Presents, 3)
    
    print("Lowest quantum entanglement: {0:d}".format(lowestQuantumEntanglement))
    print("Best solution:")
    print("  Passenger compartment: {0}".format(', '.join([str(item) for item in bestSolution[0]])))
    print("  Compartment 2: {0}".format(', '.join([str(item) for item in bestSolution[1]])))
    print("  Compartment 3: {0}".format(', '.join([str(item) for item in bestSolution[2]])))
    print("")
    print("All solutions:")
    for item in allSolutions:
        print("   ({0}) ({1}) ({2})".format(', '.join([str(item) for item in item[0]]),
                                            ', '.join([str(item) for item in item[1]]),
                                            ', '.join([str(item) for item in item[2]])))
        
    # same thing, 4 groups
    target = sum(day24Presents) / 4
    allSolutions = []
    lowestQuantumEntanglement = None
    bestSolution = None       
    
    print("\nPart 2")    
    divideIntoGroups(day24Presents, 4)
    
    print("Lowest quantum entanglement: {0:d}".format(lowestQuantumEntanglement))
    print("Best solution:")
    print("  Passenger compartment: {0}".format(', '.join([str(item) for item in bestSolution[0]])))
    print("  (the remaining compartments are left as an exercise for the reader)")