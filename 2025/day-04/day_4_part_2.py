import sys
sys.path.append('../advent-of-code')
from utils import *
import os

content = get_file_content('2025/day-04/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content), len(content[0]))

i = 0
for line in content:
    j = 0
    for char in line:
        map[i][j] = char
        j = j + 1
    i = i + 1

rolls_of_paper = 0
can_remove_rop = True
debug = True

while can_remove_rop:
    if(debug):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_map(map)
        input()
    can_remove_rop = False
    i = 0
    for line in map:
        j = 0
        for char in line:

            if(map[i][j] == "@"):
                count = 0
                if(i - 1 >= 0 and map[i - 1][j] == "@"):
                    count = count + 1
                if(i + 1 < len(map) and map[i + 1][j] == "@"):
                    count = count + 1
                if(j - 1 >= 0 and map[i][j - 1] == "@"):
                    count = count + 1
                if(j + 1 < len(map[i]) and map[i][j + 1] == "@"):
                    count = count + 1

                if(i - 1 >= 0 and j - 1 >= 0 and map[i - 1][j - 1] == "@"):
                    count = count + 1
                if(i + 1 < len(map) and j + 1 < len(map[i]) and map[i + 1][j + 1] == "@"):
                    count = count + 1
                if(i + 1 < len(map) and j - 1 >= 0 and map[i + 1][j - 1] == "@"):
                    count = count + 1
                if(i - 1 >= 0 and j + 1 < len(map[i]) and map[i - 1][j + 1] == "@"):
                    count = count + 1

                if(count < 4):
                    rolls_of_paper = rolls_of_paper + 1
                    map[i][j] = "."
                    can_remove_rop = True
            j = j + 1
        i = i + 1

print(rolls_of_paper)