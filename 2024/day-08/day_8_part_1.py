import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2024/day-08/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content), len(content[0]))
frequencies = {}
i = 0
for line in content:
    j = 0
    for char in line:
        map[i][j] = char
        if(char != "."):
            if(char not in frequencies):
                frequencies[char] = [[i, j]]
            else:
                frequencies[char].append([i, j])
        j = j + 1
    i = i + 1
    
antinodes = []

for frequency, antennas in frequencies.items():
    for antenna_1 in antennas:
        for antenna_2 in antennas:
            if(antenna_1 != antenna_2):
                x_1 = antenna_1[0]
                y_1 = antenna_1[1]

                x_2 = antenna_2[0]
                y_2 = antenna_2[1]

                antinode_1 = [x_1 + (x_1 - x_2), y_1 + (y_1 - y_2)]
                antinode_2 = [x_2 + (x_2 - x_1), y_2 + (y_2 - y_1)]

                if(antinode_1 not in antinodes and in_map(map, antinode_1)):
                    antinodes.append(antinode_1)
                if(antinode_2 not in antinodes and in_map(map, antinode_2)):
                    antinodes.append(antinode_2)

print(len(antinodes))