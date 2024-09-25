import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-3/input.txt')

map = {
  "0;0": 1
}

current_pos = "0;0"

for char in content:
    split = split_string(current_pos, ";")
    if(char == ">"):
        current_pos = split[0] + ";" + str(int(split[1]) + 1)
    elif(char == "v"):
        current_pos = str(int(split[0]) + 1) + ";" + split[1]
    elif(char == "<"):
        current_pos = split[0] + ";" + str(int(split[1]) - 1)
    elif(char == "^"):
        current_pos = str(int(split[0]) - 1) + ";" + split[1]
    else:
        print("Error: unknown character.")

    if current_pos in map:
        map[current_pos] = map[current_pos] + 1
    else: 
        map[current_pos] = 1

print(len(map))