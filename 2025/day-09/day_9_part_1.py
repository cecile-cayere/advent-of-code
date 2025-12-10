import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-09/input.txt')
content = split_string(content, "\n")

debug = True
red_tiles = []

if(debug):
    print("Initialisation.")
for line in content:
    red_tiles.append(list(map(int, split_string(line, ","))))

if(debug):
    print("Tri.")
red_tiles = sorted(red_tiles, key=lambda item: (item[0], item[1]))

max_size = 0
i = 0
if(debug):
    print("Calcul des surfaces des rectangles.")
while i < len(red_tiles):
    j = i + 1
    while j < len(red_tiles):
        size = (abs(red_tiles[i][0] - red_tiles[j][0]) + 1) * (abs(red_tiles[i][1] - red_tiles[j][1]) + 1)
        if(max_size < size):
            max_size= size
        j = j + 1
    i = i + 1

if(debug):
    print("Affichage du résultat.")
print(max_size)