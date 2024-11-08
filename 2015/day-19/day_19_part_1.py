import sys
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
        
molecules = []

for key, table in replacements.items():
    for value in table:
        i = 0
        while i < len(molecule):
            if(len(key) == 1 and key == molecule[i]):
                new_molecule = molecule[:i] + value + molecule[i + 1:]
                if(new_molecule not in molecules): molecules.append(new_molecule)
            elif(len(key) == 2 and i < len(molecule) - 1 and key == molecule[i] + molecule[i + 1]):
                new_molecule = molecule[:i] + value + molecule[i + 2:]
                if(new_molecule not in molecules): molecules.append(new_molecule)
            i = i + 1

print(len(molecules))