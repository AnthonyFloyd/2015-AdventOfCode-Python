# Day 11
# 2015-12-10
#
# Corporate policy
#

def getNextPassword(previousPassword, verbose=False):
    '''
    With the given 8 character lower-case password, increment the letters until the
    next valid password is found.
    
    Returns the next valid password.
    
    '''
    
    #
    # immediately deal with invalid passwords
    #
    
    if len(previousPassword) != 8:
        raise RuntimeError("The password must be 8 characters.")
    
    if previousPassword.lower() != previousPassword:
        raise RuntimeError("The password must be all lower case.")
    
    # now deal with invalid characters: i, o, l
    # note that checkCharacter will advance the password to the
    # next valid password if it finds an invalid password
    
    # first change the password to a list of ints
    previousPasswordInts = [ord(character) for character in previousPassword]
    
    # check we're starting with a valid password
    for counter in range(7):
        checkCharacter(previousPasswordInts, counter, verbose)
        
    # rebuild the password as a string
    nextPassword = ''.join([chr(i) for i in previousPasswordInts])
    
    #
    # Search for the next password
    #
    stillSearching = True
    while stillSearching:
        
        # increment password
        nextPassword = incrementPassword(nextPassword, verbose)
        
        # convert the password to a list of ints
        nextPasswordInts = [ord(character) for character in nextPassword]
        
        # check against the rules
        
        # increasing straight?
        hasStraight = False
        
        for counter in range(5):
            if nextPasswordInts[counter+2] == nextPasswordInts[counter+1] + 1 and \
               nextPasswordInts[counter+1] == nextPasswordInts[counter] + 1:
                hasStraight = True
                break
            
        # check for mistaken letters
        hasMistakenCharacters = False
        
        if ord('i') in nextPasswordInts: 
            hasMistakenCharacters = True
        elif ord('l') in nextPasswordInts:
            hasMistakenCharacters = True
        elif ord('o') in nextPasswordInts:
            hasMistakenCharacters = True
            
        # needs two pairs of letters
        nPairs = 0
        pairedInts = []
        
        for counter in range(7):
            if nextPasswordInts[counter] == nextPasswordInts[counter + 1]:
                if nextPasswordInts[counter] not in pairedInts:
                    nPairs += 1
                    pairedInts.append(nextPasswordInts[counter])
                
    
        # keep this password?
        if hasStraight == True and hasMistakenCharacters == False and nPairs >= 2:
            stillSearching = False
            
    if verbose: print('\r           ', end='')
    print('\rThe next password is {0}\n'.format(nextPassword))
            
    return nextPassword
            
def incrementPassword(previousPassword, verbose=False):
    '''
    Increments the last character in the password, then checks to
    see if the resulting password is valid. If it's not valid,
    the character check will advance the password to the next
    valid password.
    
    Returns the next valid password.
    
    
    '''
    
    # convert the password characters to integers
    passwordCharacters = [ord(character) for character in previousPassword]
    
    # increment last character
    passwordCharacters[7] += 1
    
    # check the password. Note that this call will fix the password
    # if the password is not valid.
    checkCharacter(passwordCharacters, 7, verbose)
    
    # rebuild the password to a string
    passwordCharacters = [chr(i) for i in passwordCharacters]
    nextPassword = ''.join(passwordCharacters)
  
    return nextPassword

def checkCharacter(passwordCharacters, index, verbose=False):
    '''
    Check the password for invalid characters starting at the given index, 
    and adjust the password if invalid characters are encountered. 
    
    If the letter rolls over past 'z', reset the character to 'a', and
    advance the previous character. Check the characters again.
    
    if the letter is an 'i','l', or 'o', advance it, and set all remaining
    characters to 'a'. Check the characters again.
    
    
    '''
    
    if verbose: print('\r{0}'.format(''.join([chr(i) for i in passwordCharacters])), end='')
    
    # check for z+1 (or {) ie, ord('z')=123
    if passwordCharacters[index] == 123: 
        passwordCharacters[index] = 97   # a
        passwordCharacters[index - 1] += 1
        checkCharacter(passwordCharacters, index-1, verbose)
    else:
        # check for i, l, o
        if passwordCharacters[index] == 105 or passwordCharacters[index] == 108 or passwordCharacters[index] == 111:
            # advanced past the illegal character
            passwordCharacters[index] += 1
            # set remaining characters to 'a'
            for counter in range(index + 1, 8):
                passwordCharacters[counter] = 97
                
            checkCharacter(passwordCharacters, index, verbose)
            
    return passwordCharacters

if __name__  == '__main__':
    
    verbose = False
    
    # tests
    print("Starting with 'abcdefgh':")
    nextPassword = getNextPassword('abcdefgh', verbose)
    
    print("Starting with 'ghijklmn':")
    nextPassword = getNextPassword('ghijklmn', verbose)

    # part 1
    print("Starting with 'hxbxwxba':")
    nextPassword = getNextPassword('hxbxwxba', verbose)
    
    # part 2
    print("Starting with '{0}'".format(nextPassword))
    nextPassword = getNextPassword(nextPassword, verbose)