#
# Advent of code
# Day 25
#
# Let It Snow
#
# To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019.
#

TARGET_ROW = 3010
TARGET_COLUMN = 3019

   #|    1         2         3         4         5         6
#---+---------+---------+---------+---------+---------+---------+
 #1 | 20151125  18749137  17289845  30943339  10071777  33511524
 #2 | 31916031  21629792  16929656   7726640  15514188   4041754
 #3 | 16080970   8057251   1601130   7981243  11661866  16474243
 #4 | 24592653  32451966  21345942   9380097  10600672  31527494
 #5 |    77061  17552253  28094349   6899651   9250759  31663883
 #6 | 33071741   6796745  25397450  24659492   1534922  27995004
 
seedNumber = 20151125
multiplier = 252533
divisor = 33554393
 
startRow = 1
currentRow = 1
currentColumn = 1
currentNumber = seedNumber

foundTarget = False
 
while not foundTarget:
   multiplied = currentNumber * multiplier
   currentNumber = multiplied % divisor
   
   currentRow -= 1
   
   # move through column
   if currentRow == 0:
      currentRow = startRow + 1
      startRow = currentRow
      currentColumn = 1
   else:
      currentColumn += 1
      
   if currentRow == TARGET_ROW and currentColumn == TARGET_COLUMN:
      break
   
print("Requested code: {0:d}".format(currentNumber))

    
 

