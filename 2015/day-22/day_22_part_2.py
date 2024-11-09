# Pas 650, 671

import sys
import json
import copy
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-22/input.txt')
content = split_string(content, "\n")

best_cost = -1

def planned_fight(boss, player, spell_list):
    turn = 0
    current_spells = {}
    cost = 0

    while boss["Hit Points"] > 0 and player["Hit Points"] > 0:
        '''if turn == 0 : print("Player turn") 
        else: print("Boss turn")
        print(boss)
        print(player)
        print(current_spells)
        print()'''
        
        for i in copy.deepcopy(current_spells).keys():
            boss["Hit Points"] = boss["Hit Points"] - current_spells[i]["Damage"]

            if(boss["Hit Points"] <= 0):
                return cost

            player["Mana"] = player["Mana"] + current_spells[i]["Mana"]

            current_spells[i]["Duration"] = current_spells[i]["Duration"] - 1
            if(current_spells[i]["Duration"] == 0):
                player["Armor"] = player["Armor"] - current_spells[i]["Armor"]
                del current_spells[i]
        
        if turn == 0:
            name = spell_list.pop(0)
            for spell in spells['Spells']:
                if(name == spell["Name"] ):
                    player["Mana"] = player["Mana"] - spell["Cost"]
                    cost = cost + spell["Cost"]
                    player["Armor"] = player["Armor"] + spell["Armor"]

                    if(spell["Duration"] == 0):
                        boss["Hit Points"] = boss["Hit Points"] - spell["Damage"]
                        if(boss["Hit Points"] <= 0):
                            return cost
                        
                        player["Hit Points"] = player["Hit Points"] + spell["Heal"]

                    else:
                        current_spells[spell["Name"]] = copy.deepcopy(spell)

                    turn = 1

        else:
            damage = boss["Damage"] - player["Armor"]
            if(damage <= 0):
                damage = 1

            player["Hit Points"] = player["Hit Points"] - damage
            if(player["Hit Points"] <= 0):
                return -1
            
            turn = 0

def fight(boss, player, current_spells, turn, cost, spell_list):
    global best_cost
    global spells

    '''if turn == 0 : print("Player turn") 
    else: print("Boss turn")
    print(boss)
    print(player)
    print(current_spells)
    print()'''

    for i in copy.deepcopy(current_spells).keys():
        boss["Hit Points"] = boss["Hit Points"] - current_spells[i]["Damage"]

        if(boss["Hit Points"] <= 0):
            #print("The player wins ! The spells casted for a cost of", cost, "was :", spell_list)
            #input()
            if(best_cost == -1 or cost < best_cost):
                best_cost = cost
            return 0

        player["Mana"] = player["Mana"] + current_spells[i]["Mana"]

        current_spells[i]["Duration"] = current_spells[i]["Duration"] - 1

        if(current_spells[i]["Duration"] == 0):
            player["Armor"] = player["Armor"] - current_spells[i]["Armor"]
            del current_spells[i]

    if turn == 0:
        player["Hit Points"] = player["Hit Points"] - 1
        if(player["Hit Points"] <= 0):
            #print("The boss wins ! The spells casted for a cost of", cost, "was :", spell_list)
            #input()
            return 1
        
        for spell in spells['Spells']:
            copy_boss = copy.deepcopy(boss)
            copy_player = copy.deepcopy(player)
            copy_current_spells = copy.deepcopy(current_spells)

            if(spell["Name"] not in copy_current_spells and copy_player["Mana"] >= spell["Cost"] and (best_cost == -1 or cost + spell["Cost"] < best_cost)):
                copy_player["Mana"] = copy_player["Mana"] - spell["Cost"]
                copy_player["Armor"] = copy_player["Armor"] + spell["Armor"]

                if(spell["Duration"] == 0):
                    copy_boss["Hit Points"] = copy_boss["Hit Points"] - spell["Damage"]
                    if(copy_boss["Hit Points"] <= 0):
                        #print("The player wins ! The spells casted for a cost of", cost, "was :", spell_list)
                        #input()
                        best_cost = cost + spell["Cost"]
                        return 0
                    
                    copy_player["Hit Points"] = copy_player["Hit Points"] + spell["Heal"]

                else:
                    copy_current_spells[spell["Name"]] = copy.deepcopy(spell)

                fight(copy_boss, copy_player, copy_current_spells, 1, cost + spell["Cost"], spell_list + [spell["Name"]])
    else:
        damage = boss["Damage"] - player["Armor"]
        if(damage <= 0):
            damage = 1

        player["Hit Points"] = player["Hit Points"] - damage
        if(player["Hit Points"] <= 0):
            #print("The boss wins ! The spells casted for a cost of", cost, "was :", spell_list)
            #input()
            return 1
        
        fight(copy.deepcopy(boss), copy.deepcopy(player), copy.deepcopy(current_spells), 0, cost, spell_list)

spells = json.loads(json.dumps({'Spells': [ {'Name': 'Magic Missile',   'Cost': 53,  'Duration': 0, 'Damage': 4, 'Armor': 0, 'Heal': 0, 'Mana': 0},
                                            {'Name': 'Poison',          'Cost': 173, 'Duration': 6, 'Damage': 3, 'Armor': 0, 'Heal': 0, 'Mana': 0}, 
                                            {'Name': 'Drain',           'Cost': 73,  'Duration': 0, 'Damage': 2, 'Armor': 0, 'Heal': 2, 'Mana': 0}, 
                                            {'Name': 'Shield',          'Cost': 113, 'Duration': 6, 'Damage': 0, 'Armor': 7, 'Heal': 0, 'Mana': 0}, 
                                            {'Name': 'Recharge',        'Cost': 229, 'Duration': 5, 'Damage': 0, 'Armor': 0, 'Heal': 0, 'Mana': 101}]}))

'''
player = {'Hit Points': 10, 
          'Damage': 0, 
          'Armor': 0, 
          'Mana': 250}
boss = {'Hit Points': 14, 
        'Damage': 8}

print(planned_fight(boss, player, ["Recharge", "Shield", "Drain", "Poison", "Magic Missile"]))
'''

player = {'Hit Points': 50, 
          'Damage': 0, 
          'Armor': 0, 
          'Mana': 500}
boss = {}

for line in content:
    line = split_string(line, ": ")
    boss[line[0]] = int(line[1])
boss["Armor"] = 0

fight(boss, player, {}, 0, 0, [])
print(best_cost)