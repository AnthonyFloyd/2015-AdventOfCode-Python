# Day 14
# 2015-12-13
#

day14Input='''Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.
'''

day14Test='''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
'''

testLines = day14Test.splitlines()
inputLines = day14Input.splitlines()

class Reindeer(object):
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.location = 0
        self.isResting = False
        self.timeCounter = 0
        self.points = 0
                
def buildListOfReindeer(inputLines):
        
    reindeer = []
    for line in inputLines:
        lineBits = line.split()
        name, speed, duration, rest = (lineBits[0], int(lineBits[3]), int(lineBits[6]), int(lineBits[13]))
        newReindeer = Reindeer(name, speed, duration, rest)
        reindeer.append(newReindeer)
        
    return reindeer

#timePeriod = 1000
timePeriod = 2503

reindeers = buildListOfReindeer(inputLines)
farthestReindeer = 0

for time in range(timePeriod):
    currentTime = time + 1
    
    for reindeer in reindeers:
        if reindeer.isResting == False:
            reindeer.location += reindeer.speed
            reindeer.timeCounter += 1
            
            if reindeer.location > farthestReindeer:
                farthestReindeer = reindeer.location
            
            if reindeer.timeCounter >= reindeer.duration:
                reindeer.isResting = True
                reindeer.timeCounter = 0
        else:
            reindeer.timeCounter += 1
            if reindeer.timeCounter >= reindeer.rest:
                reindeer.isResting = False
                reindeer.timeCounter = 0
    
    for reindeer in reindeers:            
        if reindeer.location == farthestReindeer:
            reindeer.points += 1

maxPoints = 0
for reindeer in reindeers:
    if reindeer.points > maxPoints:
        maxPoints = reindeer.points
        
print("The farthest reindeer is at {0:d} km".format(farthestReindeer))
print("... and has {0:d} points.".format(maxPoints))

