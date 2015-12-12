# Day 9
# 2015-12-08
#
# All in a single night
#
# Brute-force method
# Not too slow, good enough
#

import itertools

debug = False

testInputs = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''

day9Inputs = '''AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90
'''

def findRoutes(distances, debug=False):
    #
    # Build map
    #
    
    cities = {} # StartCity: {DestinationCity: distance}
    
    for distance in distances:
        distanceBits = distance.split()
        
        # forward travel
        if cities.get(distanceBits[0], False):
            cities[distanceBits[0]][distanceBits[2]] = int(distanceBits[4])
        else:
            cities[distanceBits[0]] = {distanceBits[2]:int(distanceBits[4])}
            
        # backward travel
        if cities.get(distanceBits[2], False):
            cities[distanceBits[2]][distanceBits[0]] = int(distanceBits[4])
        else:
            cities[distanceBits[2]] = {distanceBits[0]:int(distanceBits[4])}
            
    #
    # get all the possible routes between the cities
    #
         
    routes = itertools.permutations(cities.keys(), len(cities))
    
    #
    # Evaluate each route, finding the distances, picking out the min, max
    #
    
    shortestDistance = 1e6
    shortestRoute = None
    
    longestDistance = 0
    longestRoute = None
    
    for route in routes:
        distance = 0
        for counter in range(len(route) - 1):
            city1 = route[counter]
            city2 = route[counter + 1]
            distance += cities[city1][city2]
            
        if distance < shortestDistance:
            shortestDistance = distance
            shortestRoute = route
            
        if distance > longestDistance:
            longestDistance = distance
            longestRoute = route
        
        if debug: print("Route: {0}\nDistance: {1}".format(",".join(route), distance))
            
    print("Shortest distance is: {0:d}".format(shortestDistance))
    print("Shortest route is: {0}".format(", ".join(shortestRoute)))
    print("Longest distance is: {0:d}".format(longestDistance))
    print("Longest route is: {0}".format(", ".join(longestRoute)))
    
if __name__ == '__main__':
    
    # test inputs
    print("Test distances")
    distances = testInputs.splitlines()
    findRoutes(distances)
    
    print("")
    
    print("Actual distances")
    distances = day9Inputs.splitlines()    
    findRoutes(distances)
    