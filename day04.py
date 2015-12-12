#!/bin/python

# Advent of Code
# Day 4
# 2015-12-03

import hashlib

startString = b'bgvyzdsv'

number = 0
foundNumber = False
fiveNumber = None
sixNumber = None

while not foundNumber:
    if number % 1000 == 0:
        print('%d...' % number)
        
    testString = b'%s%d' % (startString, number)
    digest = hashlib.md5(testString).hexdigest()
    
    if fiveNumber is None:
        if digest[:5] == '00000':
            fiveNumber = number
    elif digest[:6] == '000000':
        sixNumber = number
        foundNumber = True
    
    number += 1
        
print("Smallest 5 number is: %d" % fiveNumber)
print("Smallest 6 number is: %d" % sixNumber)
