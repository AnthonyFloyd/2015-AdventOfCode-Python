#
# Advent of Code
# Day 21
#

ITEM_TYPE_WEAPON = 0
ITEM_TYPE_ARMOUR = 1
ITEM_TYPE_RING = 2

class Fighter(object):
    def __init__(self, name='', armour=0, hitPoints=0, damage=0, money=0, rings=None, armourWorn=None, weapon=None):
        self.name = name
        self.armour = armour
        self.hitPoints = hitPoints
        self.startHitPoints = hitPoints
        
        self.damage = damage
        self.money = money

        if rings is None:
            rings = []
            
        self.rings = []
        
        for ring in rings:
            self.wearRing(ring)
            
        self.wornArmour = None
        
        if armourWorn is not None:
            self.donArmour(armourWorn)
            
        self.weapon = None
        
        if weapon is not None:
            self.wieldWeapon(weapon)
               
    def wearRing(self, ring):
        success = True
        if ring is not None:
            if len(self.rings) < 2:
                self.damage += ring.damage
                self.armour += ring.armour
                self.money -= ring.cost
                self.rings.append(ring)
            else:
                success = False
            
        return success
    
    def donArmour(self, armour):
        success = True
        if self.wornArmour is None:
            self.damage += armour.damage
            self.armour += armour.armour
            self.money -= armour.cost
            self.wornArmour = armour
        else:
            success = False
            
        return success
    
    def wieldWeapon(self, weapon):
        success = True
        if self.weapon is None:
            self.damage += weapon.damage
            self.armour += weapon.armour
            self.money -= weapon.cost
            self.weapon = weapon
        else:
            success = False
            
        return success

class Item(object):
    def __init__(self, name='', itemType=None, cost=0, damage=0, armour=0):
        self.cost = cost
        self.damage = damage
        self.armour = armour
        self.name = name
        self.type = itemType
        
class Weapon(Item):
    def __init__(self, name, cost, damage, armour):
        Item.__init__(self, name, ITEM_TYPE_WEAPON, cost, damage, armour)
        
class Armour(Item):
    def __init__(self, name, cost, damage, armour):
        Item.__init__(self, name, ITEM_TYPE_ARMOUR, cost, damage, armour)
        
class Ring(Item):
    def __init__(self, name, cost, damage, armour):
        Item.__init__(self, name, ITEM_TYPE_RING, cost, damage, armour)
        
class Store(object):
    def __init__(self, weapons=None, armour=None, rings=None):
        if weapons is None:
            weapons = []
            
        if armour is None:
            armour = []
            
        if rings is None:
            rings = []
        
        self.weapons = weapons
        self.armour = armour
        self.rings = rings
    
    def getWeapons(self):
        return self.weapons
    
    def getArmour(self):
        return self.armour
    
    def getRings(self):
        return self.rings
    
    def buyWeapon(self, weapon):
        self.weapons.remove(weapon)
        
    def buyArmour(self, armour):
        self.armour.remove(armour)
        
    def buyRing(self, ring):
        self.rings.remove(ring)
        
    def addWeapon(self, weapon):
        self.weapons.append(weapon)
        
    def addArmour(self, armour):
        self.armour.append(armour)
        
    def addRing(self, ring):
        self.rings.append(ring)
        
def resolveBattle(player, boss, verbose=False):
    
    while True:
        # player first
        damage = max(1, player.damage - boss.armour)
        boss.hitPoints -= damage
        if verbose: print("Player strikes! Boss incurs {0:d} damage ({1:d} HP left)".format(damage, boss.hitPoints))
        if boss.hitPoints <= 0:
            winner = player
            if verbose: print("Player wins!")
            break
        
        # now the boss
        damage = max(1, boss.damage - player.armour)
        player.hitPoints -= damage
        if verbose: print("Boss strikes! Player incurs {0:d} damage ({1:d} HP left)".format(damage, player.hitPoints))
        if player.hitPoints <= 0:
            winner = boss
            if verbose: print("Boss wins! Boo!")
            break

    return winner
        
#
# Store
#
#Weapons:    Cost  Damage  Armor  Damage/Cost
#Dagger        8     4       0       0.5
#Shortsword   10     5       0       0.5
#Warhammer    25     6       0       0.24
#Longsword    40     7       0       0.175
#Greataxe     74     8       0       0.108108

#Armor:      Cost  Damage  Armor  Armour/Cost
#Leather      13     0       1       0.0769
#Chainmail    31     0       2       0.0645
#Splintmail   53     0       3       0.0566
#Bandedmail   75     0       4       0.0533
#Platemail   102     0       5       0.0490

#Rings:      Cost  Damage  Armor   Damage|Armour/Cost
#Damage +1    25     1       0       0.04
#Damage +2    50     2       0       0.04
#Damage +3   100     3       0       0.03
#Defense +1   20     0       1       0.05
#Defense +2   40     0       2       0.05
#Defense +3   80     0       3       0.0375

store = Store()
store.addWeapon(Weapon('Dagger', 8, 4, 0))
store.addWeapon(Weapon('Shortsword', 10, 5, 0))
store.addWeapon(Weapon('Warhammer', 25, 6, 0))
store.addWeapon(Weapon('Longsword', 40, 7, 0))
store.addWeapon(Weapon('Greataxe', 74, 8, 0))

store.addArmour(Armour('Leather', 13, 0, 1))
store.addArmour(Armour('Chainmail', 31, 0, 2))
store.addArmour(Armour('Splintmail', 53, 0, 3))
store.addArmour(Armour('Bandedmail', 75, 0, 4))
store.addArmour(Armour('Platemail', 102, 0, 5))

store.addRing(Ring('Damage +1', 25, 1, 0))
store.addRing(Ring('Damage +2', 50, 2, 0))
store.addRing(Ring('Damage +3', 100, 3, 0))
store.addRing(Ring('Defense +1', 20, 0, 1))
store.addRing(Ring('Defense +2', 40, 0, 2))
store.addRing(Ring('Defense +3', 80, 0, 3))

# test input
testPlayer = Fighter(name='Player', armour=5, hitPoints=8, damage=5)
testBoss = Fighter(name='Boss', armour=2, hitPoints=12, damage=7)

print("Test case:")
winner  = resolveBattle(testPlayer, testBoss, verbose=True)
print("{0} won the battle\n".format(winner.name))

# actual input
# Hit Points: 103
# Damage: 9
# Armor: 2
        
boss = Fighter(name='Boss',armour=2, damage=9, hitPoints=103)

#
# Brute force the rest 
#

weapons = store.getWeapons() # need at least 1 weapon
armour = store.getArmour() # 0 or 1
armour.insert(0, Armour('None',0,0,0))

rings = store.getRings() # 0, 1, or 2
rings.insert(0, Ring('None',0,0,0))
rings.insert(0, Ring('None',0,0,0))

lowestCost = 1E6
highestCost = 0

for weapon in weapons:
    for armourItem in armour:
        for ring1 in rings:
            remainingRings = [ring for ring in rings if ring != ring1]
            for ring2 in remainingRings:
                newPlayer = Fighter(name='Player',
                                    hitPoints=100,
                                    weapon=weapon,
                                    armourWorn=armourItem,
                                    rings=[ring1, ring2]
                                    )
                boss.hitPoints = boss.startHitPoints
                
                winner = resolveBattle(newPlayer, boss)
                cost = abs(newPlayer.money)
                if winner == newPlayer:
                    if cost < lowestCost:
                        lowestCost = cost
                        lowestCostFighter = newPlayer
                        lowestCostFighter.hitPoints = lowestCostFighter.startHitPoints
                else:
                    if cost > highestCost:
                        highestCost = cost
                        highestCostFighter = newPlayer
                        highestCostFighter.hitPoints = highestCostFighter.startHitPoints
                    
print("Lowest cost win: {0:d}".format(lowestCost))
print("Player items")
print("Weapon: {0}".format(lowestCostFighter.weapon.name))
print("Armour: {0}".format(lowestCostFighter.wornArmour.name))
print("Ring 1: {0}".format(lowestCostFighter.rings[0].name))
print("Ring 2: {0}".format(lowestCostFighter.rings[1].name))
print("Player stats: HP: {0:d} Damage: {1:d} Armour: {2:d}".format(lowestCostFighter.hitPoints,
                                                                   lowestCostFighter.damage,
                                                                   lowestCostFighter.armour))
print("")

print("Highest cost loss: {0:d}".format(highestCost))
print("Player items")
print("Weapon: {0}".format(highestCostFighter.weapon.name))
print("Armour: {0}".format(highestCostFighter.wornArmour.name))
print("Ring 1: {0}".format(highestCostFighter.rings[0].name))
print("Ring 2: {0}".format(highestCostFighter.rings[1].name))
print("Player stats: HP: {0:d} Damage: {1:d} Armour: {2:d}".format(highestCostFighter.hitPoints,
                                                                   highestCostFighter.damage,
                                                                   highestCostFighter.armour))

                        
                        
        