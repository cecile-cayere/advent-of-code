import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2024/day-05/input.txt')
content = split_string(content, "\n")

rules = []
updates = []
switch = False

i = 0
for line in content:
    if(switch == False):
        if(line == ""):
            switch = True
        else:
            page_1, page_2 = split_string(line, "|")
            rules.append([int(page_1), int(page_2)])

    else:
        line = split_string(line, ",")
        updates.append(list(map(lambda n: int(n), line)))

rules_tmp = list(rules)

sum = 0
for update in updates:
    is_valid = True
    for rule in rules:
        if(rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1])):
            is_valid = False
            break

    if(is_valid == False):
        corrected_update = []
        for element in update:
            if(len(corrected_update) == 0):
                corrected_update.append(element)

            else:
                inserted = False
                j = 0
                while not inserted and j < len(corrected_update):
                    for rule in rules:
                        if(rule[0] == element and rule[1] == corrected_update[j]):
                            corrected_update.insert(corrected_update.index(corrected_update[j]), element)
                            inserted = True
                    j = j + 1

                if(not inserted):
                    corrected_update.append(element)

        sum = sum + corrected_update[int(len(corrected_update)/2)]
    
print(sum)