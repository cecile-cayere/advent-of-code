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

    if(is_valid == True):
        sum = sum + update[int(len(update)/2)]
    
print(sum)

'''
# This function creates a list of all existing elements, trying to respect all the rules. This doesn't work, as there are triplets of unsolvable rules.
order = []

while len(rules_tmp) > 0:
    page_1 = int(rules_tmp[0][0])
    page_2 = int(rules_tmp[0][1])

    if(len(order) == 0):
        order.append(page_1)
        order.append(page_2)

    else:
        if(page_1 not in order):
            inserted = False
            j = 0
            while not inserted and j < len(order):
                for rule in rules:
                    if(rule[0] == page_1 and rule[1] == order[j]):
                        #print("rule:", rule)
                        order.insert(order.index(order[j]), page_1)
                        inserted = True
                j = j + 1

            if(not inserted):
                order.append(page_1)

        if(page_2 not in order):
            inserted = False
            j = 0
            while not inserted and j < len(order):
                for rule in rules:
                    #print("rule:", rule)
                    if(rule[0] == page_2 and rule[1] == order[j]):
                        order.insert(order.index(order[j]), page_2)
                        inserted = True
                j = j + 1

            if(not inserted):
                order.append(page_2)

    rules_tmp.remove(rules_tmp[0])

print(order)
'''