#
# Advent of Code
# Day 22
#

from day21 import Fighter
from copy import deepcopy as copy

leastMana = 3000
winningPlayer = None

SPELL_LIST = ['Recharge',
              'Shield',
              'Drain',
              'Poison',
              'Magic Missile',
              ]

class Wizard(Fighter):
    def __init__(self, name='', armour=0, hitPoints=0, damage=0, mana=0):
        Fighter.__init__(self, name=name, armour=armour, hitPoints=hitPoints, 
                         damage=damage, money=0, rings=None, armourWorn=None, 
                         weapon=None)
        
        self.mana = mana
        self.startMana = mana
        
        self.spentMana = 0
        self.castSpells = []
        
        self.activeSpells =[]
        
    def getAvailableSpells(self):
        activeSpellNames = [spell.name for spell in self.activeSpells if spell.duration > 1]
        availableSpells = [spell for spell in SPELL_LIST if spell not in activeSpellNames]
        filteredSpells = [spell for spell in availableSpells if SPELLS[spell].cost < self.mana]
        
        return filteredSpells
    
    def reset(self):
        Fighter.rest(self)
        self.mana = self.startMana
        self.spentMana = 0
        self.castSpells = []
        self.activeSpells = []
        
    def castSpell(self, spellName, defender, verbose=False):
        spell = SPELLS[spellName]
        
        assert isinstance(spell, Spell)

        if spell.cost >= self.mana:
            if verbose: print("{0} doesn't have enough mana to cast {1}!".format(self.name,
                                                                                 spellName))
            return False
        
        if verbose: print("{0} casts {1} at a cost of {2:d} mana".format(self.name,
                                                                         spellName,
                                                                         spell.cost))
        self.mana -= spell.cost 
        self.spentMana += spell.cost
        self.castSpells.append(spellName)
        
        if spell.duration == 0:
            if spell.damage > 0:
                if verbose: print("{0} takes {1:d} damage from the {2} spell".format(defender.name,
                                                                                     spell.damage,
                                                                                     spell.name))
                defender.hitPoints -= spell.damage
            if spell.heal > 0:
                if verbose: print("{0} heals {1:d} from the {2} spell".format(self.name,
                                                                              spell.heal,
                                                                              spell.name))
                self.hitPoints += spell.heal
        else:
            self.activeSpells.append(spell.cast())

        return True
        
    
class Spell(object):
    def __init__(self, name, cost=0, damage=0, heal=0, armour=0,
                 duration=0, mana=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.armour = armour
        self.duration = duration
        self.mana = mana
    
        self.timer = 0
        
    def cast(self):
        newSpell = Spell(self.name, 
                         cost=self.cost, 
                         damage=self.damage, 
                         heal=self.heal, 
                         armour=self.armour, 
                         duration=self.duration,
                         mana=self.mana)
        return newSpell
    
SPELLS = {'Magic Missile': Spell('Magic Missle', cost=53, damage=4),
          'Drain': Spell('Drain', cost=73, damage=2, heal=2),
          'Shield': Spell('Shield', cost=113, armour=7, duration=6),
          'Poison': Spell('Poison', cost=173, damage=3, duration=6),
          'Recharge': Spell('Recharge', cost=229, mana=101, duration=5),
          }    

def evaluateTurn(attacker, defender, newSpell=None, verbose=False):
    #
    # 
    #
    
    if verbose:
        print("\n{0} turn".format(attacker.name))
        if isinstance(attacker, Wizard):
            print("{0} has {1:d} HP, {2:d} armour, {3:d} mana".format(attacker.name,
                                                                      attacker.hitPoints,
                                                                      attacker.armour,
                                                                      attacker.mana))
        else:
            print("{0} has {1:d} HP, {2:d} attack".format(attacker.name,
                                                          attacker.hitPoints,
                                                          attacker.damage))
            

        print("{0} has {1:d} HP, {2:d} armour".format(defender.name,
                                                      defender.hitPoints,
                                                      defender.armour))

    #
    # Build up attack
    #
    
    attackValue = attacker.damage
    defenseValue = defender.armour
    
    # evaluate instant spells
    
    if newSpell is not None:
        #if verbose:
            #print("{0} casts {1}".format(attacker.name,
                                         #newSpell))
        attacker.castSpell(newSpell, defender, verbose=verbose)
    
    # evaluate active spells
    if isinstance(attacker, Wizard):
        wizard = attacker
        target = defender
    else:
        wizard = defender
        target = attacker
        
    newSpells = []
    for spell in wizard.activeSpells:
        if spell.name != newSpell:
            if spell.damage > 0:
                if verbose: print("{0} does {1:d} damage and ".format(spell.name,
                                                                      spell.damage),
                                  end='')
                target.hitPoints -= spell.damage

            
            if spell.armour > 0:
                if verbose: print("{0} increases {1}'s armour by {2:d} and ".format(spell.name,
                                                                                    wizard.name,
                                                                                    spell.armour),
                                  end='')
                if wizard == defender:
                    defenseValue += spell.armour
                
                
            if spell.mana > 0:
                if verbose: print("{0} increases {1}'s mana by {2:d} and ".format(spell.name,
                                                                                  wizard.name,
                                                                                  spell.mana),
                                  end='')
                wizard.mana += spell.mana
            
            spell.duration -= 1
            if spell.duration > 0:
                newSpells.append(spell)
                if verbose: print("will continue for {0:d} turns.".format(spell.duration))
            else:
                if verbose: print("its effects end.")
                
        else:
            newSpells.append(spell)
            
    wizard.activeSpells = newSpells
    
    if defender.hitPoints > 0 and attacker.hitPoints > 0:
        # evaluate battle
        if attackValue > 0:
            damage = max(1, attackValue - defenseValue)
            defender.hitPoints -= damage
            
            if verbose: print("{0} loses {1:d} hit points!".format(defender.name,
                                                                   damage))
def battleRound(player, boss, spell, verbose=True):
    winner = None
    loser = None
    
    player.hitPoints -= 1
    if player.hitPoints > 0:
        evaluateTurn(player, boss, spell, verbose=verbose)
        
    if boss.hitPoints <= 0:
        winner = player
        loser = boss
        
    elif player.hitPoints <= 0:
        winner = boss
        loser = player
    
    if winner is None:
        evaluateTurn(boss, player, verbose=verbose)
        if boss.hitPoints <= 0:
            winner = player
            loser = boss
            
        elif player.hitPoints <= 0:
            winner = boss
            loser = player
            
    #if winner == player:
        #print('{0} won, {1:d} HP remaining'.format(winner.name,
                                                   #winner.hitPoints))
            
    return winner

def tryAllSpells(player, boss, verbose=True):
    
    global leastMana, winningPlayer
    
    availableSpells = player.getAvailableSpells()
    
    for spell in availableSpells:
        clonedPlayer = copy(player)
        clonedBoss = copy(boss)
        if len(clonedPlayer.castSpells) < 4:
            print("The trial spells start with: {0}".format(', '.join(clonedPlayer.castSpells)))
        
        winner = battleRound(clonedPlayer, clonedBoss, spell, verbose=verbose)
        
        if winner is None:
            if clonedPlayer.spentMana < leastMana:
                tryAllSpells(clonedPlayer, clonedBoss, verbose=verbose)
            #else:
                #print("Too much mana, aborting")

        elif winner == clonedPlayer:
            if clonedPlayer.spentMana < leastMana:
                leastMana = clonedPlayer.spentMana
                winningPlayer = clonedPlayer
                print("********************************************************")
                print("Minimum mana: {0:d}".format(leastMana), flush=True)
                print("The spells for this win are: {0}".format(', '.join(winningPlayer.castSpells)))
                print("********************************************************")
                if not verifyWin(winningPlayer.castSpells):
                    raise RuntimeError("Won but didn't win. Huh?")
            #else:
                #print("{0:d}, ".format(clonedPlayer.spentMana), end='')
                

def verifyWin(spellList, verbose=False):
    player = Wizard('Player', hitPoints=50, mana=500)
    boss = Fighter('Boss', hitPoints=58, damage=9)        
                      
    winner = None
    playerSpells = copy(spellList)
    
    while winner is None:
        if len(playerSpells) > 0:
            newSpell = playerSpells.pop(0)
        else:
            newSpell = None
            
        winner = battleRound(player, boss, newSpell, verbose=verbose)
        
    if player.hitPoints > 0:
        if verbose: print("{0} wins!".format(player.name))
        return True
    else:
        if verbose: print("{0} is defeated. :|".format(player.name))       
        return False
                
            
#
# Test script 1       
#           
        
print("********")        
print("BATTLE 1")
print("********\n")

player = Wizard('Player', hitPoints=10, mana=250)
boss = Fighter('Boss', hitPoints=13, damage=8)        
                  
playerSpells = ['Poison', 'Magic Missile']
winner = None

while winner is None:
    if len(playerSpells) > 0:
        newSpell = playerSpells.pop(0)
    else:
        newSpell = None
    
    winner = battleRound(player, boss, newSpell, verbose=True)
        
    
if player.hitPoints > 0:
    print("{0} wins!".format(player.name))
else:
    print("{0} is defeated. :|".format(player.name))
    
                
#
# Test script 2    
#           
        
print("\n********")        
print("BATTLE 2")
print("********\n")
        
player = Wizard('Player', hitPoints=10, mana=250)
boss = Fighter('Boss', hitPoints=14, damage=8)        
                  
playerSpells = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile']
winner = None

while winner is None:
    if len(playerSpells) > 0:
        newSpell = playerSpells.pop(0)
    else:
        newSpell = None
        
    winner = battleRound(player, boss, newSpell)
    
if player.hitPoints > 0:
    print("{0} wins!".format(player.name))
else:
    print("{0} is defeated. :|".format(player.name))
    
#
# 1415: wrong?
# 1269 is right.
    
#print("\n********")        
#print("TEST BATTLE")
#print("********\n")
        
#player = Wizard('Player', hitPoints=50, mana=500)
#boss = Fighter('Boss', hitPoints=58, damage=9)        
                  
#spellList = "Recharge, Poison, Shield, Recharge, Magic Missile, Poison, Shield, Magic Missile, Magic Missile, Poison, Magic Missile"
#playerSpells = [item.strip() for item in spellList.split(',')]
#winner = None

#while winner is None:
    #if len(playerSpells) > 0:
        #newSpell = playerSpells.pop(0)
    #else:
        #newSpell = None
        
    #winner = battleRound(player, boss, newSpell, verbose=True)
    
#if player.hitPoints > 0:
    #print("{0} wins, spending {1:d} mana!".format(player.name,
                                                   #player.spentMana))
#else:
    #print("{0} is defeated. :|".format(player.name))    
    
#
# Part 1
# Least amount of mana and still win
#           
        
print("\n********")        
print("PART 1")
print("********\n")

player = Wizard('Player', hitPoints=50, mana=500)
boss = Fighter('Boss', hitPoints=58, damage=9)   

leastMana, winningPlayer = tryAllSpells(player, boss, verbose=False)

if leastMana < 1000000 and winningPlayer is not None:
    print("The least mana for a win is: {0:d} ({1:d})".format(leastMana, winningPlayer.spentMana))
    print("The spells for this win are: {0}".format(', '.join(winningPlayer.castSpells)))
else:
    print("Didn't find a solution")

                            
                
    
                        
                        
        