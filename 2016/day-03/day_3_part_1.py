import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2016/day-03/input.txt')
content = split_string(content, "\n")

triangles = []

for line in content:
    triangle = line.split()
    triangles.append([int(triangle[0]), int(triangle[1]), int(triangle[2])])

count = 0

for triangle in triangles:
    if(is_segments_triangle(triangle)):
        count = count + 1
    
print(count)