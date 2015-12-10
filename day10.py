# Day 9
# 2015-12-08
#
# Look say
#

testInput = 1
day10Input = 1113222113

def lookSay(inputString):
    
    outputString = ''
    
    previousCharacter = None
    previousCounter = 0
    
    for character in inputString:
        if character != previousCharacter:
            if previousCharacter != None:
                outputString += '{0:d}{1}'.format(previousCounter, previousCharacter)
                previousCharacter = character
                previousCounter = 1
            else:
                previousCharacter = character
                previousCounter = 1                
        else:
            previousCounter += 1
                
    #
    # Include the last character
    #
    outputString += '{0:d}{1}'.format(previousCounter, character)

    return outputString

# test inputs
testString = '{0:d}'.format(testInput)
for counter in range(5):
    testString = lookSay(testString)
    
print('Length of test input after 5 iterations: {0:d}'.format(len(testString)))
        
# part 1
testString = '{0:d}'.format(day10Input)
for counter in range(40):
    testString = lookSay(testString)
    
print('Length of string after 40 iterations: {0:d}'.format(len(testString)))

# part 2
for counter in range(10):
    testString = lookSay(testString)
    
print('Length of string after 50 iterations: {0:d}'.format(len(testString)))