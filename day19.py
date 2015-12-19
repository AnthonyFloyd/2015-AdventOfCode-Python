#
# Advent of Code
# Day 19
# Medicine For Rudolph
#

day19Input = '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg
'''

day19Start = '''CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF
'''

testInput = '''H => HO
H => OH
O => HH
'''

testStart = 'HOHOHO'

testInput2 = '''e => H
e => O
H => HO
H => OH
O => HH
'''

testStart2 = 'e'
testTarget = 'HOHOHO'

def getTransformations(inputList):
    '''
    Build a dict of how one element can transform into another.
    
    A single element may transform into multiple forms.
    Expects list of lines of the form "e => Ne" where "e" is 
    the starting state, and "Ne" is the transformed state.
        
    '''
    
    transformations = {} # e: [Ne, Me, Be]
    
    for line in inputList:
        lineBits = line.split()
        # line: e => Ne
        key, value = lineBits[0], lineBits[2]
        
        if transformations.get(key, None) is None:
            transformations[key] = [value,]
        else:
            transformations[key].append(value)
            
    return transformations

def findall(subString, searchString):
    """
    Find all occurances of subString in searchString,
    return list of indices of start of subString.
    
    """
    
    assert isinstance(searchString, str)
    
    locations = []
    length = len(searchString)
    location = 0
    startLocation = 0
    
    while location != -1:
        location = searchString.find(subString, startLocation)
        if location > -1:
            locations.append(location)
            startLocation += len(subString)
            
    return locations

def getMolecules(start, transformations):
    """
    Find all the molecules that could be formed by taking the start molecule
    and applying all the transformations.
    
    Returns a unique list of next-generation molecules.
    
    """
    assert isinstance(transformations, dict)
    assert isinstance(start, str)
    
    molecules = []
    
    for key,valueList in transformations.items():
        keyLength = len(key)
        locations = findall(key, start)
        
        for replacement in valueList:
            for location in locations:
                newMolecule = start[0:location] + replacement + start[location+keyLength:]
                molecules.append(newMolecule)
                
    return molecules

def getSteps(startMolecule, targetMolecule, transformations):
    """
    Get the number of steps required to transform the start molecule into
    the target molecule, with the given tranformation rules.
    
    """
    #
    # Initially tried forward method, but becomes untractable
    #
    #molecules=[startMolecule,]
    #newMolecules = []
    #counter = 0
    #stillSearching = True
    
    #while stillSearching and counter < 100:
        
        #counter += 1
        #print("Iteration {1:d}, starting with {0:d} molecules".format(len(molecules), counter))

        #for molecule in molecules:
            #additionalMolecules = getMolecules(molecule, transformations)
            #if targetMolecule in additionalMolecules:
                #stillSearching = False
                #break
            
            #newMolecules.extend(additionalMolecules)
            
        #molecules = list(set(newMolecules))
        
        
    #if stillSearching == True:
        #print('Unable to find target molecule.')
        
    #print('')
    
    #
    # Let's try backward method
    #
    
    # invert dict, create reverse lookup
    
    reverseLookup = {}
    
    for key, valueList in transformations.items():
        for v in valueList:
            if reverseLookup.get(v, None) is None:
                reverseLookup[v] = key
            else:
                raise RuntimeError("Unfortunately the reverse lookup is not unique")
            
    # with the reverse lookup, sort the keys by length
    
    allKeys = sorted(reverseLookup.keys(),key=lambda x: len(x))
    
    currentKeys = [i for i in allKeys]
    
    # now reverse the molecule by replacing items in the starting molecule, starting with the
    # longest replacement, going down to the shortest
    
    counter = 0
    currentMolecule = targetMolecule
    assert isinstance(currentMolecule, str)
    poppedTargets = []
    
    while currentMolecule != startMolecule and len(currentKeys) > 0:
        replacementTarget = currentKeys.pop()
        poppedTargets.append(replacementTarget)
        if currentMolecule.find(replacementTarget) >= 0:
            #print("{0} => ".format(currentMolecule), end='')
            currentMolecule = currentMolecule.replace(replacementTarget, reverseLookup[replacementTarget],1)
            #print("{0}".format(currentMolecule))
            
            counter += 1
            currentKeys.extend(reversed(poppedTargets))
            poppedTargets = []
            #print("{0:d}".format(counter))
            
    if currentMolecule.strip() != startMolecule:
        print("Couldn't figure it out")
            
    return counter

def test(verbose=True):
    """
    Run the test inputs.
    
    """
    
    # test
    inputList = testInput.splitlines()
    transformations = getTransformations(inputList)
    molecules = getMolecules(testStart, transformations)
    moleculeSet = set(molecules)
    if verbose: print("{0:d} distinct molecules were generated in the test.".format(len(moleculeSet)))
    #print(moleculeSet)

def part1(verbose=True):
    """
    Run the part 1 inputs.
    
    """
    # part 1
    inputList = day19Input.splitlines()
    transformations = getTransformations(inputList)
    molecules = getMolecules(day19Start, transformations)
    moleculeSet = set(molecules)

    if verbose: print("{0:d} distinct molecules were generated in part 1.".format(len(moleculeSet)))

def part2_test(verbose=True):
    """
    Run the test for part 2.
    
    """
    # part 2 test
    inputList = testInput2.splitlines()
    transformations = getTransformations(inputList)
    requiredSteps = getSteps(testStart2, testTarget, transformations)
    if verbose: print("\n{0:d} steps are required to go from {1} to {2}.".format(requiredSteps, testStart2, testTarget))

def part2(verbose=True):
    """
    Run the part 2 inputs.
    
    """
    # part 2 
    inputList = day19Input.splitlines()
    transformations = getTransformations(inputList)
    requiredSteps = getSteps('e', day19Start, transformations)
    if verbose: print("\n{0:d} steps are required to go from {1} to {2}.".format(requiredSteps, testStart2, day19Start))
    
def runall(verbose=True):
    """
    Run both part 1 and part 2.
    
    """
    
    part1(verbose)
    part2(verbose)

if __name__ == '__main__':
    test()
    part1()
    part2_test()
    part2()
    
    


