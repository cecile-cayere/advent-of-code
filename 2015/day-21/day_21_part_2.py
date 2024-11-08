import sys
import json
import copy
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-21/input.txt')
content = split_string(content, "\n")

def fight(boss, player, debug = False):
    turn = 0
    while boss["Hit Points"] > 0 and player["Hit Points"] > 0:
        if turn == 0:
            damage = player["Damage"] - boss["Armor"]
            if(damage <= 0):
                damage = 1
            boss["Hit Points"] = boss["Hit Points"] - damage
            if(debug): print("The player deals", player["Damage"], "-", boss["Armor"], "=", damage, "damage; the boss goes down to", boss["Hit Points"], "hit points.")
            turn = 1
        else:
            damage = boss["Damage"] - player["Armor"]
            if(damage <= 0):
                damage = 1
            player["Hit Points"] = player["Hit Points"] - damage
            if(debug): print("The boss deals", boss["Damage"], "-", player["Armor"], "=", damage, "damage; the player goes down to", player["Hit Points"], "hit points.")
            turn = 0

    if(boss["Hit Points"] <= 0):
        if(debug): print("The player wins !")
        return True
    else:
        if(debug): print("The boss wins !")
        return False


boss = {}
player = {'Hit Points': 100, 
          'Damage': 0, 
          'Armor': 0}

shop = json.loads(json.dumps(
    {'Weapons': [{'Name': 'Dagger',     'Cost': 8,      'Damage': 4, 'Armor': 0}, 
                 {'Name': 'Shortsword', 'Cost': 10,     'Damage': 5, 'Armor': 0}, 
                 {'Name': 'Warhammer',  'Cost': 25,     'Damage': 6, 'Armor': 0}, 
                 {'Name': 'Longsword',  'Cost': 40,     'Damage': 7, 'Armor': 0}, 
                 {'Name': 'Greataxe',   'Cost': 74,     'Damage': 8, 'Armor': 0}],
    'Armor':    [{'Name': 'None',       'Cost': 0,      'Damage': 0, 'Armor': 0}, 
                 {'Name': 'Leather',    'Cost': 13,     'Damage': 0, 'Armor': 1}, 
                 {'Name': 'Chainmail',  'Cost': 31,     'Damage': 0, 'Armor': 2}, 
                 {'Name': 'Splintmail', 'Cost': 53,     'Damage': 0, 'Armor': 3}, 
                 {'Name': 'Bandedmail', 'Cost': 75,     'Damage': 0, 'Armor': 4}, 
                 {'Name': 'Platemail',  'Cost': 102,    'Damage': 0, 'Armor': 5}],
    'Rings':    [{'Name': 'None 1',     'Cost': 0,      'Damage': 0, 'Armor': 0}, 
                 {'Name': 'None 2',     'Cost': 0,      'Damage': 0, 'Armor': 0}, 
                 {'Name': 'Damage +1',  'Cost': 25,     'Damage': 1, 'Armor': 0}, 
                 {'Name': 'Damage +2',  'Cost': 50,     'Damage': 2, 'Armor': 0}, 
                 {'Name': 'Damage +3',  'Cost': 100,    'Damage': 3, 'Armor': 0}, 
                 {'Name': 'Defense +1', 'Cost': 20,     'Damage': 0,  'Armor': 1}, 
                 {'Name': 'Defense +2', 'Cost': 40,     'Damage': 0,  'Armor': 2}, 
                 {'Name': 'Defense +3', 'Cost': 80,     'Damage': 0,  'Armor': 3}
                  ]}))

for line in content:
    line = split_string(line, ": ")
    boss[line[0]] = int(line[1])
    

max_cost = -1
for weapon in shop["Weapons"]:
    for armor in shop["Armor"]:
        for ring_1 in shop["Rings"]:
            for ring_2 in shop["Rings"]:
                if(ring_1["Name"] != ring_2["Name"]):
                    total_cost = weapon["Cost"] + armor["Cost"] + ring_1["Cost"] + ring_2["Cost"]
                    player['Damage'] = weapon["Damage"] + armor["Damage"] + ring_1["Damage"] + ring_2["Damage"]
                    player['Armor'] = weapon["Armor"] + armor["Armor"] + ring_1["Armor"] + ring_2["Armor"]
                else:
                    total_cost = -1

                fight_result = fight(copy.deepcopy(boss), copy.deepcopy(player), False)
                if(total_cost != -1 and max_cost == -1 and not fight_result) or (total_cost != -1 and max_cost != -1 and total_cost > max_cost and not fight_result):
                    max_cost = total_cost

print(max_cost)