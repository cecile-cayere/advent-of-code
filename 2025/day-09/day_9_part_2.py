import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-09/input.txt')
content = split_string(content, "\n")

debug = False
red_tiles = []

if(debug):
    print("Initialisation.")
for line in content:
    red_tiles.append(list(map(int, split_string(line, ","))))

green_tiles = []
i = 0
if(debug):
    print("Définition des dalles vertes sur les contours,")
while i < len(red_tiles) - 1:
    if(red_tiles[i][0] == red_tiles[i + 1][0]):
        min_green_tiles = min(red_tiles[i][1], red_tiles[i + 1][1]) + 1
        max_green_tiles = max(red_tiles[i][1], red_tiles[i + 1][1])
        for j in range(min_green_tiles, max_green_tiles):
            green_tiles.append([red_tiles[i][0], j])
            
    elif(red_tiles[i][1] == red_tiles[i + 1][1]):
        min_green_tiles = min(red_tiles[i][0], red_tiles[i + 1][0]) + 1
        max_green_tiles = max(red_tiles[i][0], red_tiles[i + 1][0])
        for j in range(min_green_tiles, max_green_tiles):
            green_tiles.append([j, red_tiles[i][1]])
    i = i + 1

if(red_tiles[i][0] == red_tiles[0][0]):
    min_green_tiles = min(red_tiles[i][1], red_tiles[0][1]) + 1
    max_green_tiles = max(red_tiles[i][1], red_tiles[0][1])
    for j in range(min_green_tiles, max_green_tiles):
        green_tiles.append([red_tiles[i][0], j])
        
elif(red_tiles[i][1] == red_tiles[0][1]):
    min_green_tiles = min(red_tiles[i][0], red_tiles[0][0]) + 1
    max_green_tiles = max(red_tiles[i][0], red_tiles[0][0])
    for j in range(min_green_tiles, max_green_tiles):
        green_tiles.append([j, red_tiles[i][1]])

if(debug):
    print("Tri.")
red_tiles = sorted(red_tiles, key=lambda item: (item[0], item[1]))

i = 0
rectangles = {}
if(debug):
    print("Calcul des surfaces des rectangles.")
while i < len(red_tiles):
    j = i + 1
    while j < len(red_tiles):
        key = str(i) + "-" + str(j)
        size = (abs(red_tiles[i][0] - red_tiles[j][0]) + 1) * (abs(red_tiles[i][1] - red_tiles[j][1]) + 1)
        rectangles[key] = size
        j = j + 1
    i = i + 1
rectangles = dict(sorted(rectangles.items(), key=lambda item: item[1], reverse=True))

max_size = 0
for key, value in rectangles.items():
    is_inside = True
    indexes = split_string(key, "-")
    index_1 = int(indexes[0])
    index_2 = int(indexes[1])

    red_tile_1 = red_tiles[index_1]
    red_tile_2 = red_tiles[index_2]


    for green_tile in green_tiles:
        if(green_tile[0] >= red_tile_1[0] + 1 and 
           green_tile[0] < red_tile_2[0] - 1 and 
           green_tile[1] >= min(red_tile_1[1], red_tile_2[1]) + 1 and 
           green_tile[1] < max(red_tile_1[1], red_tile_2[1])):
            is_inside = False

    if is_inside:
        max_size = value
        break

    i = i + 1

if(debug):
    print("Affichage du résultat.")
print(max_size)