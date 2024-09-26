import sys
sys.path.append('../advent-of-code')
from utils import *

import hashlib

content = get_file_content('2015/day-6/input.txt')
content = split_string(content, "\n")

lights = init_2_dim_list(1000, 1000)

for instruction in content:
    if instruction.startswith("turn off"):
        start = split_string(split_string(instruction, "turn off ")[1], " through ")[0]
        end = split_string(split_string(instruction, "turn off ")[1], " through ")[1]

        i = int(split_string(start, ",")[0])
        while i <= int(split_string(end, ",")[0]):
            j = int(split_string(start, ",")[1])
            while j <= int(split_string(end, ",")[1]):
                lights[i][j] = 0
                j = j + 1
            i = i + 1
        
    elif instruction.startswith("turn on"):
        start = split_string(split_string(instruction, "turn on ")[1], " through ")[0]
        end = split_string(split_string(instruction, "turn on ")[1], " through ")[1]

        i = int(split_string(start, ",")[0])
        while i <= int(split_string(end, ",")[0]):
            j = int(split_string(start, ",")[1])
            while j <= int(split_string(end, ",")[1]):
                lights[i][j] = 1
                j = j + 1
            i = i + 1

    elif instruction.startswith("toggle"):
        start = split_string(split_string(instruction, "toggle ")[1], " through ")[0]
        end = split_string(split_string(instruction, "toggle ")[1], " through ")[1]

        i = int(split_string(start, ",")[0])
        while i <= int(split_string(end, ",")[0]):
            j = int(split_string(start, ",")[1])
            while j <= int(split_string(end, ",")[1]):
                if(lights[i][j] == 1) :
                    lights[i][j] = 0
                else:
                    lights[i][j] = 1
                j = j + 1
            i = i + 1
    else:
        print("Error: unknown instruction \"" + instruction + "\"")
    

print(count_values_in_2_dim_list(lights, 1))