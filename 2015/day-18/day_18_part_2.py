import sys
import copy
import os
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-18/input.txt')
content = split_string(content, "\n")

def count_neighbors(lights, x, y):
    count = 0
    if(x > 0):
        if(y > 0 and lights[x - 1][y - 1] == "#"): count = count + 1
        if(lights[x - 1][y] == "#"): count = count + 1
        if(y < len(lights[x]) - 1 and lights[x - 1][y + 1] == "#"): count = count + 1
    if(x < len(lights) - 1):
        if(y > 0 and lights[x + 1][y - 1] == "#"): count = count + 1
        if(lights[x + 1][y] == "#"): count = count + 1
        if(y < len(lights[x]) - 1 and lights[x + 1][y + 1] == "#"): count = count + 1
    if(y > 0 and lights[x][y - 1] == "#"): count = count + 1
    if(y < len(lights[x]) - 1 and lights[x][y + 1] == "#"): count = count + 1
    return(count)

lights = []
i = 0
for line in content:
    lights.append([])
    for light in line:
        lights[i].append(light)
    i = i + 1

#os.system('cls')
#print_map(lights)

lights[0][0] = "#"
lights[0][len(lights[0]) - 1] = "#"
lights[len(lights) - 1][0] = "#"
lights[len(lights) - 1][len(lights[0]) - 1] = "#"

i = 0
while i < 100:
    x = 0
    new_lights = copy.deepcopy(lights)
    while x < len(lights):
        y = 0
        while y < len(lights[x]):
            if not ((x == 0 and y == 0) or 
                    (x == 0 and y == len(lights[0]) - 1) or 
                    (x == len(lights) - 1 and y == 0) or 
                    (x == len(lights) - 1 and y == len(lights[0]) - 1)):
                neighbors = count_neighbors(lights, x, y)
                if(lights[x][y] == "#" and neighbors != 2 and neighbors != 3):
                    new_lights[x][y] = "."
                elif(lights[x][y] == "." and neighbors == 3):
                    new_lights[x][y] = "#"
            y = y + 1
        x = x + 1
    i = i + 1
    lights = copy.deepcopy(new_lights)
    #os.system('cls')
    #print_map(lights)

count = 0
x = 0
while x < len(lights):
    y = 0
    while y < len(lights[x]):
        if(lights[x][y] == "#"):
           count = count + 1
        y = y + 1
    x = x + 1

print(count)
