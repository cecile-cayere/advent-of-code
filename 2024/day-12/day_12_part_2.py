import sys
sys.path.append('../advent-of-code')
from utils import *

plots = []
edges = []
def get_area(map, plot):
    x = plot[0]
    y = plot[1]
    plots.append(plot)
    area = 1
    
    if(x - 1 >= 0 and map[x][y] == map[x - 1][y]):
        if([x - 1, y] not in plots):
            area = area + get_area(map, [x - 1, y])
    else:
        edge = ([x, y], "N")
        if(edge not in edges):
            edges.append(edge)


    if(y + 1 < len(map[x]) and map[x][y] == map[x][y + 1]):
        if([x, y + 1] not in plots):
            area = area + get_area(map, [x, y + 1])
    else:
        edge = ([x, y], "E")
        if(edge not in edges):
            edges.append(edge)


    if(x + 1 < len(map) and map[x][y] == map[x + 1][y]):
        if([x + 1, y] not in plots):
            area = area + get_area(map, [x + 1, y])
    else:
        edge = ([x, y], "S")
        if(edge not in edges):
            edges.append(edge)


    if(y - 1 >= 0 and map[x][y] == map[x][y - 1]):
        if([x, y - 1] not in plots):
            area = area + get_area(map, [x, y - 1])
    else:
        edge = ([x, y], "W")
        if(edge not in edges):
            edges.append(edge)

    return area


content = get_file_content('2024/day-12/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content), len(content[0]))

i = 0
for line in content:
    j = 0
    for char in line:
        map[i][j] = char
        j = j + 1
    i = i + 1

price = 0
i = 0
for line in map:
    j = 0
    for plot in line:
        if [i, j] not in plots:
            edges = []
            area = get_area(map, [i, j])
            edges.sort()

            sides = []
            for edge in edges:
                x = edge[0][0]
                y = edge[0][1]
                dir = edge[1]

                added = False

                for side in sides:
                    for edge_2 in side:
                        if( ((dir == "E" or dir == "W") and (([x - 1, y], dir) == edge_2 or ([x + 1, y], dir) == edge_2)) or 
                            ((dir == "N" or dir == "S") and (([x, y - 1], dir) == edge_2 or ([x, y + 1], dir) == edge_2))):
                            side.append(edge)
                            added = True

                if(not added):
                    sides.append([edge])

            price = price + (area * len(sides))
        j = j + 1
    i = i + 1

print(price)