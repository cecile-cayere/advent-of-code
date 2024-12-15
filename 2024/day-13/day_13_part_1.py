import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2024/day-13/input.txt')
content = split_string(content, "\n")
claw_machines = []

i = 0
claw_machines.append({})
for line in content:
    if line == "":
        i = i + 1
        claw_machines.append({})
    elif("Button A" in line):
        line = split_string(line, ": ")
        x, y = split_string(line[1], ", ")
        x = int(split_string(x, "X+")[1])
        y = int(split_string(y, "Y+")[1])
        claw_machines[i]["A"] = [x, y]
    elif("Button B" in line):
        line = split_string(line, ": ")
        x, y = split_string(line[1], ", ")
        x = int(split_string(x, "X+")[1])
        y = int(split_string(y, "Y+")[1])
        claw_machines[i]["B"] = [x, y]
    else:
        line = split_string(line, ": ")
        x, y = split_string(line[1], ", ")
        x = int(split_string(x, "X=")[1])
        y = int(split_string(y, "Y=")[1])
        claw_machines[i]["Prize"] = [x, y]

total_tokens = 0
for claw_machine in claw_machines:
    x = 0
    y = 0
    game_tokens = 0
    end_game = False

    i = 0
    while i < 100 and not end_game:
        j = 0
        while j < 100 and not end_game:
            x = (i * claw_machine["A"][0]) + (j * claw_machine["B"][0])
            y = (i * claw_machine["A"][1]) + (j * claw_machine["B"][1])
            game_tokens = (i * 3) + (j * 1)

            if(x == claw_machine["Prize"][0] and y == claw_machine["Prize"][1]):
                end_game = True
                total_tokens = total_tokens + game_tokens
            j = j + 1
        i = i + 1

print(total_tokens)