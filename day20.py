# Advent of Code
# Day 20
#

day20Input = 33100000

def findFactors(inputNumber):
    factors = set()
    for factor in range(1, int(inputNumber**0.5) + 1):
        if inputNumber%factor == 0:
            factors.add(int(factor))
            factors.add(int(inputNumber / factor))
    return factors

if __name__ == "__main__":

    # part 1
    target = day20Input / 10
    
    currentNumber = target // 10
    
    while True:
        factors = findFactors(int(currentNumber))
        total = sum(factors)
        if total >= target:
            break
        currentNumber += 1
        
    print("Part 1: {0:d}".format(int(currentNumber)))
    
    #currentNumber = int(776160)
    # part 2
    target = day20Input 
    
    # start from the last solution. This one will be bigger
    while True:
        factors = findFactors(int(currentNumber))
        total = 0
        for factor in factors:
            #
            # weed out the tired reindeer
            #
            numberTotalVisits = currentNumber // factor
            if numberTotalVisits < 50:
                total += factor * 11
            
        if total >= target:
            break
        
        currentNumber += 1    

    
    print("Part 2: {0:d}".format(int(currentNumber)))