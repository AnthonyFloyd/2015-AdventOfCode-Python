# Day 13
# 2015-12-12
#

import itertools

testInputs='''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
'''

day13Inputs='''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 81 happiness units by sitting next to Carol.
Alice would lose 42 happiness units by sitting next to David.
Alice would gain 89 happiness units by sitting next to Eric.
Alice would lose 89 happiness units by sitting next to Frank.
Alice would gain 97 happiness units by sitting next to George.
Alice would lose 94 happiness units by sitting next to Mallory.
Bob would gain 3 happiness units by sitting next to Alice.
Bob would lose 70 happiness units by sitting next to Carol.
Bob would lose 31 happiness units by sitting next to David.
Bob would gain 72 happiness units by sitting next to Eric.
Bob would lose 25 happiness units by sitting next to Frank.
Bob would lose 95 happiness units by sitting next to George.
Bob would gain 11 happiness units by sitting next to Mallory.
Carol would lose 83 happiness units by sitting next to Alice.
Carol would gain 8 happiness units by sitting next to Bob.
Carol would gain 35 happiness units by sitting next to David.
Carol would gain 10 happiness units by sitting next to Eric.
Carol would gain 61 happiness units by sitting next to Frank.
Carol would gain 10 happiness units by sitting next to George.
Carol would gain 29 happiness units by sitting next to Mallory.
David would gain 67 happiness units by sitting next to Alice.
David would gain 25 happiness units by sitting next to Bob.
David would gain 48 happiness units by sitting next to Carol.
David would lose 65 happiness units by sitting next to Eric.
David would gain 8 happiness units by sitting next to Frank.
David would gain 84 happiness units by sitting next to George.
David would gain 9 happiness units by sitting next to Mallory.
Eric would lose 51 happiness units by sitting next to Alice.
Eric would lose 39 happiness units by sitting next to Bob.
Eric would gain 84 happiness units by sitting next to Carol.
Eric would lose 98 happiness units by sitting next to David.
Eric would lose 20 happiness units by sitting next to Frank.
Eric would lose 6 happiness units by sitting next to George.
Eric would gain 60 happiness units by sitting next to Mallory.
Frank would gain 51 happiness units by sitting next to Alice.
Frank would gain 79 happiness units by sitting next to Bob.
Frank would gain 88 happiness units by sitting next to Carol.
Frank would gain 33 happiness units by sitting next to David.
Frank would gain 43 happiness units by sitting next to Eric.
Frank would gain 77 happiness units by sitting next to George.
Frank would lose 3 happiness units by sitting next to Mallory.
George would lose 14 happiness units by sitting next to Alice.
George would lose 12 happiness units by sitting next to Bob.
George would lose 52 happiness units by sitting next to Carol.
George would gain 14 happiness units by sitting next to David.
George would lose 62 happiness units by sitting next to Eric.
George would lose 18 happiness units by sitting next to Frank.
George would lose 17 happiness units by sitting next to Mallory.
Mallory would lose 36 happiness units by sitting next to Alice.
Mallory would gain 76 happiness units by sitting next to Bob.
Mallory would lose 34 happiness units by sitting next to Carol.
Mallory would gain 37 happiness units by sitting next to David.
Mallory would gain 40 happiness units by sitting next to Eric.
Mallory would gain 18 happiness units by sitting next to Frank.
Mallory would gain 7 happiness units by sitting next to George.
'''

def createHappinessDict(inputs):
    '''
    Create a mapping of relative happiness.
    
    
    '''
    
    assert isinstance(inputs, list)
    
    happinessDict = {}
    
    for line in inputs:
        lineBits = line.split()
        
        # line format:
        # {name1} would {gain|lose} {0} happiness units by sitting next to {name2}.
        
        (name1, direction, happiness, name2) = (lineBits[0], lineBits[2], int(lineBits[3]), lineBits[10][:-1])
        
        if direction == 'lose':
            happiness *= -1
            
        if happinessDict.get(name1, None) is None:
            happinessDict[name1] = {name2:happiness}
        else:
            happinessDict[name1][name2] = happiness
            
    return happinessDict

def optimizeSeating(happinessDict):
    '''
    Given a happiness map, find the optimal seating arrangement.
    
    
    '''
    
    allNames = happinessDict.keys()
    nNames = len(allNames)
    
    allArrangements = itertools.permutations(allNames, nNames)
    
    bestHappiness = 0
    bestArrangement = None
    
    for arrangementIter in allArrangements:
        arrangement = list(arrangementIter)        
        arrangement.append(arrangement[0])
        currentHappiness = 0
        
        for counter in range(nNames):
            currentHappiness += happinessDict[arrangement[counter]][arrangement[counter+1]]
            currentHappiness += happinessDict[arrangement[counter+1]][arrangement[counter]]
            
        if currentHappiness > bestHappiness:
            bestHappiness = currentHappiness
            bestArrangement = arrangement
            
    #print("Best happiness: {0}".format(bestHappiness))
    #print("Best arrangement: {0}".format(bestArrangement))
    
    return bestHappiness, bestArrangement

if __name__ == '__main__':
    
    #
    # test
    #
    
    testInputList = testInputs.splitlines()
    happinessDict = createHappinessDict(testInputList)
    bestHappiness, bestArrangement = optimizeSeating(happinessDict)
    
    print("Test")
    print("The best happiness is: {0:d}".format(bestHappiness))
    print("The optimal seating pattern is: {0}".format(bestArrangement))
    
    #
    # day13, part 1
    #
    
    inputList = day13Inputs.splitlines()
    happinessDict = createHappinessDict(inputList)
    bestHappiness, bestArrangement = optimizeSeating(happinessDict)
    
    print("\nPart 1")
    print("The best happiness is: {0:d}".format(bestHappiness))
    print("The optimal seating pattern is: {0}".format(bestArrangement))
    
    # day 13, part 2, add me, everyone is ambivalent
    
    allNames = happinessDict.keys()
    myName = 'Anthony'
    happinessDict[myName] = {}
    
    for name in allNames:
        happinessDict[name][myName] = 0
        happinessDict[myName][name] = 0
    
    bestHappiness, bestArrangement = optimizeSeating(happinessDict)
    
    print("\nPart 2")
    print("The best happiness is: {0:d}".format(bestHappiness))
    print("The optimal seating pattern is: {0}".format(bestArrangement))