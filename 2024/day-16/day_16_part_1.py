import sys
sys.path.append('../advent-of-code')
from utils import *
import copy

tiles = []
tmp_map = []

def browse_maze(maze, position, direction):
    x, y = position

    tiles.append([position, direction])
    if(maze[x][y] == "E"):
        return 0
    else: 
        scores = []
        if(direction == "N"):
            if(maze[x - 1][y] != "#"): 
                score = browse_maze(maze, [x - 1, y], "N")
                if(score != -1): scores.append(1 + score)
            if(maze[x][y + 1] != "#"): 
                score = browse_maze(maze, [x, y + 1], "E")
                if(score != -1): scores.append(1000 + 1 + score)
            if(maze[x][y - 1] != "#"): 
                score = browse_maze(maze, [x, y - 1], "W")
                if(score != -1): scores.append(1000 + 1 + score)

        elif(direction == "E"):
            if(maze[x - 1][y] != "#"): 
                score = browse_maze(maze, [x - 1, y], "N")
                if(score != -1): scores.append(1000 + 1 + score)
            if(maze[x][y + 1] != "#"): 
                score = browse_maze(maze, [x, y + 1], "E")
                if(score != -1): scores.append(1 + score)
            if(maze[x + 1][y] != "#"): 
                score = browse_maze(maze, [x + 1, y], "S")
                if(score != -1): scores.append(1000 + 1 + score)

        elif(direction == "S"):
            if(maze[x][y + 1] != "#"): 
                score = browse_maze(maze, [x, y + 1], "E")
                if(score != -1): scores.append(1000 + 1 + score)
            if(maze[x + 1][y] != "#"): 
                score = browse_maze(maze, [x + 1, y], "S")
                if(score != -1): scores.append(1 + score)
            if(maze[x][y - 1] != "#"): 
                score = browse_maze(maze, [x, y - 1], "W")
                if(score != -1): scores.append(1000 + 1 + score)

        else:
            if(maze[x - 1][y] != "#"): 
                score = browse_maze(maze, [x - 1, y], "N")
                if(score != -1): scores.append(1000 + 1 + score)
            if(maze[x + 1][y] != "#"): 
                score = browse_maze(maze, [x + 1, y], "S")
                if(score != -1): scores.append(1000 + 1 + score)
            if(maze[x][y - 1] != "#"): 
                score = browse_maze(maze, [x, y - 1], "W")
                if(score != -1): scores.append(1 + score)

        if(scores != []):
            print(scores)
            tmp_map[x][y] = min(scores)
            return(min(scores))
        else:
            return -1

content = get_file_content('2024/day-16/sample.txt')
content = split_string(content, "\n")

map = []
start = []
end = []
i = 0

for line in content:
    map.append([])
    j = 0
    for char in line:
        map[i].append(char)
        if(char == "S"):
            start = [i, j]
        if(char == "E"):
            end = [i, j]
        j = j + 1
    i = i + 1

tmp_map = copy.deepcopy(map)

print_map(map)
print(browse_maze(map, start, "E"))