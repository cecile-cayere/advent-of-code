import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-23/input.txt')
content = split_string(content, "\n")
instructions = []
registers = {"a": 1, "b": 0}

i = 0
for line in content:
    line = split_string(line, " ")
    instructions.append([])

    if(len(line) == 3):
        instructions[i].append(line[0])
        instructions[i].append(line[1][:-1])
        instructions[i].append(int(line[2]))
        
    else: 
        instructions[i].append(line[0])
        if(line[0] == "jmp"): instructions[i].append(int(line[1]))
        else: instructions[i].append(line[1])
    i += 1

i = 0
while i < len(instructions):
    instruction = instructions[i][0]

    if(instruction == "jio"):
        register = instructions[i][1]
        offset = instructions[i][2]
        if(registers[register] == 1):
            i = i + offset
        else:
            i += 1

    elif(instruction == "inc"):
        register = instructions[i][1]
        registers[register] = registers[register] + 1
        i += 1

    elif(instruction == "tpl"):
        register = instructions[i][1]
        registers[register] = registers[register] * 3
        i += 1

    elif(instruction == "jmp"):
        offset = instructions[i][1]
        i = i + offset

    elif(instruction == "hlf"):
        register = instructions[i][1]
        registers[register] = int(registers[register] / 2)
        i += 1

    elif(instruction == "jie"):
        register = instructions[i][1]
        offset = instructions[i][2]
        if(registers[register] % 2 == 0):
            i = i + offset
        else:
            i += 1

    else:
        i += 1

print(registers["b"])