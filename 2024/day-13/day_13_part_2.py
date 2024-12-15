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
        claw_machines[i]["Prize"] = [x + 10000000000000, y + 10000000000000]

total_tokens = 0
for claw_machine in claw_machines:
    ax, ay = claw_machine["A"]
    bx, by = claw_machine["B"]
    px, py = claw_machine["Prize"]

    i = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
    j = (px - (ax * i)) / bx

    if(int(i) == i and int(j) == j):
        total_tokens = total_tokens + (int(i) * 3) + (int(j) * 1)

print(total_tokens)