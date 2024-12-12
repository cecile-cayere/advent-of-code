import sys
sys.path.append('../advent-of-code')
from utils import *

plots = []
def get_area(map, plot):
    x = plot[0]
    y = plot[1]

    plots.append(plot)

    perimeter = 0
    area = 1
    if(x - 1 >= 0 and map[x][y] == map[x - 1][y]):
        if([x - 1, y] not in plots):
            result = get_area(map, [x - 1, y])
            area = area + result[0]
            perimeter = perimeter + result[1]
    else:
        perimeter = perimeter + 1
    if(y + 1 < len(map[x]) and map[x][y] == map[x][y + 1]):
        if([x, y + 1] not in plots):
            result = get_area(map, [x, y + 1])
            area = area + result[0]
            perimeter = perimeter + result[1]
    else:
        perimeter = perimeter + 1
    if(x + 1 < len(map) and map[x][y] == map[x + 1][y]):
        if([x + 1, y] not in plots):
            result = get_area(map, [x + 1, y])
            area = area + result[0]
            perimeter = perimeter + result[1]
    else:
        perimeter = perimeter + 1
    if(y - 1 >= 0 and map[x][y] == map[x][y - 1]):
        if([x, y - 1] not in plots):
            result = get_area(map, [x, y - 1])
            area = area + result[0]
            perimeter = perimeter + result[1]
    else:
        perimeter = perimeter + 1

    return (area, perimeter)


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
            result = get_area(map, [i, j])
            price = price + (result[0] * result[1])
        j = j + 1
    i = i + 1

print(price)