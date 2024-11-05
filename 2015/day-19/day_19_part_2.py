import sys
import copy
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-19/input.txt')
content = split_string(content, "\n")
replacements = {}
molecule = ""
    
for line in content:
    if(" => " in line):
        line = split_string(line, " => ")
        if(line[0] not in replacements):
            replacements[line[0]] = []
        replacements[line[0]].append(line[1])

    elif(line != ""):
        molecule = line

# This solution works because of the way the exercise was created, but it would be preferable to find a solution that works in the case where there's no need to make all the replacements possible. That said, I'm too lazy to do that c:

nb_steps = 0

while molecule != "e":
    for key, table in replacements.items():
        for value in table:
            new_molecule = molecule.replace(value, key, 1)
            if new_molecule != molecule:
                nb_steps += 1
                molecule = new_molecule

print(nb_steps)
