import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-07/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content[0]), len(content))

i = 0
for line in content:
    j = 0
    for char in line:
        map[i][j] = char
        j = j + 1
    i = i + 1

count = 0
i = 0
while i < len(map) - 1:
    j = 0
    while j < len(map[0]):
        if (map[i][j] == "S" or map[i][j] == "|"):
            if(map[i + 1][j] == "."):
                map[i + 1][j] = "|"
            elif(map[i + 1][j] == "^"):
                count = count + 1
                map[i + 1][j - 1] = "|"
                map[i + 1][j + 1] = "|"
                
        j = j + 1
    i = i + 1
print(count)