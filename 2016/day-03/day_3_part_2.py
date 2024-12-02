import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2016/day-03/input.txt')
content = split_string(content, "\n")

triangles = []

triangle_1 = []
triangle_2 = []
triangle_3 = []

for line in content:
    triangle = line.split()

    triangle_1.append(int(triangle[0]))
    triangle_2.append(int(triangle[1]))
    triangle_3.append(int(triangle[2]))

    if(len(triangle_1) == 3):
        triangles.append(triangle_1)
        triangles.append(triangle_2)
        triangles.append(triangle_3)
        triangle_1 = []
        triangle_2 = []
        triangle_3 = []

count = 0

for triangle in triangles:
    if(is_segments_triangle(triangle)):
        count = count + 1
    
print(count)