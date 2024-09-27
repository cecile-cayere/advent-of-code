import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-9/input.txt')
content = split_string(content, "\n")

distances_graph = {}
locations_table = []
longest_distance = -1

for line in content:
    line = split_string(line, " = ")
    locations = split_string(line[0], " to ")
    distance = int(line[1])

    if(locations[0] not in distances_graph): distances_graph[locations[0]] = {}
    distances_graph[locations[0]][locations[1]] = distance
    if(locations[1] not in distances_graph): distances_graph[locations[1]] = {}
    distances_graph[locations[1]][locations[0]] = distance

    if(locations[0] not in locations_table):
        locations_table.append(locations[0])
    if(locations[1] not in locations_table):
        locations_table.append(locations[1])

paths = permute_lst(locations_table, 0)

for path in paths:
    distance = 0
    i = 0

    while i < len(path) - 1:
        distance = distance + distances_graph[path[i]][path[i + 1]]
        i = i + 1

    if(longest_distance == -1 or distance > longest_distance):
        longest_distance = distance

print(longest_distance)
