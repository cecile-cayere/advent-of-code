import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-13/input.txt')
content = split_string(content, "\n")

def compute_happiness(arrangement, happinesses):

    happiness = happinesses[arrangement[len(arrangement) - 1]][arrangement[0]]
    i = 1
    while(i < len(arrangement)):
        happiness = happiness + happinesses[arrangement[i]][arrangement[i - 1]]
        i = i + 1
    
    return(happiness)

happinesses = {}
people = []

for line in content:
    line = split_string(line, " happiness units by sitting next to ")

    if "gain" in line[0]: 
        tmp = split_string(line[0], " would gain ")
        person_1 = tmp[0]
        happiness = int(tmp[1])
    else:
        tmp = split_string(line[0], " would lose ")
        person_1 = tmp[0]
        happiness = -1 * int(tmp[1])
    
    person_2 = split_string(line[1], ".")[0]

    if(person_1 not in people):
        people.append(person_1)
    if(person_2 not in people):
        people.append(person_2)


    if(person_1 in happinesses and person_2 in happinesses[person_1]):
        happinesses[person_1][person_2] = happinesses[person_1][person_2] + happiness

    elif(person_1 in happinesses):
        happinesses[person_1][person_2] = happiness

    else:
        happinesses[person_1] = {}
        happinesses[person_1][person_2] = happiness

    if(person_2 in happinesses and person_1 in happinesses[person_2]):
        happinesses[person_2][person_1] = happinesses[person_2][person_1] + happiness
    

    elif(person_2 in happinesses):
        happinesses[person_2][person_1] = happiness

    else:
        happinesses[person_2] = {}
        happinesses[person_2][person_1] = happiness

possibilities = permute_lst(people, 0)

best_happiness = -1

for possibility in possibilities:
    happiness = compute_happiness(possibility, happinesses)
    if(best_happiness == -1 or best_happiness < happiness):
        best_happiness = happiness

print(best_happiness)