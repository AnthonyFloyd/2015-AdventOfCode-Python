# Day 15
# 2015-12-14
#
# Science for Hungry People
#

day15Inputs='''Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
'''

day15TestInputs='''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
'''

class Ingredient(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        
def parseInput(inputList):
    
    ingredients = []
    
    for line in inputList:
        line = line.replace(',','')
        line = line.replace(':','')
        lineBits = line.split()
        # Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
        name, capacity, durability, flavor, texture, calories = (lineBits[0], int(lineBits[2]), int(lineBits[4]), int(lineBits[6]),
                                                                 int(lineBits[8]), int(lineBits[10]))
        ingredient = Ingredient(name, capacity, durability, flavor, texture, 
                               calories)
        ingredients.append(ingredient)
        
    return ingredients

def calculateCookieScore(ingredients, amounts):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    
    for counter in range(len(ingredients)):
        ingredient = ingredients[counter]
        amount = amounts[counter]
        # Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
        capacity += ingredient.capacity * amount
        durability += ingredient.durability * amount
        flavor += ingredient.flavor * amount
        texture += ingredient.texture * amount
        
    totalScore = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
    
    return totalScore
  
def calculateCookieCalories(ingredients, amounts):
    calories = 0
    
    for counter in range(len(ingredients)):
        ingredient = ingredients[counter]
        amount = amounts[counter]
        # Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
        calories += ingredient.calories * amount
    
    return calories
        

inputList = day15Inputs.splitlines()
#inputList = day15TestInputs.splitlines()

ingredients = parseInput(inputList)

maxScore = 0

# test data, only 2 ingredients
#for counter1 in range(0,100):
    #counter2 = 100 - counter1
    #score = calculateCookieScore(ingredients, (counter1, counter2))
    #if score > maxScore:
        #maxScore = score
        #maxScoreRecipe = (counter1, counter2)

# actual data, 4 ingredients                    
for counter1 in range(0,100):
    for counter2 in range(0,100-counter1):
        for counter3 in range(0,max(0,100-(counter1+counter2))):
            counter4 = 100 - counter1 - counter2 - counter3
            if counter4 < 0:
                continue
            
            score = calculateCookieScore(ingredients, (counter1, counter2, counter3, counter4))
            calories = calculateCookieCalories(ingredients, (counter1, counter2, counter3, counter4))
            
            if score > maxScore and calories == 500:
                maxScore = score
                maxScoreRecipe = (counter1, counter2, counter3, counter4)
                    
print("Maximum score: {0:d}".format(maxScore))

# test report
#print("Recipe: {0:d} {1}, {2:d} {3}".format(maxScoreRecipe[0],
                                            #ingredients[0].name,
                                            #maxScoreRecipe[1],
                                            #ingredients[1].name,
                                            #))
                                            
# actual report
print("Recipe: {0:d} {1}, {2:d} {3}, {4:d} {5}, {6:d} {7}".format(maxScoreRecipe[0],
                                                                  ingredients[0].name,
                                                                  maxScoreRecipe[1],
                                                                  ingredients[1].name,
                                                                  maxScoreRecipe[2],
                                                                  ingredients[2].name,
                                                                  maxScoreRecipe[3],
                                                                  ingredients[3].name))
