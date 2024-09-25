import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-1/input.txt')

floor = 0

for char in content:
    if(char == "("):
        floor = floor + 1
    elif(char == ")"):
        floor = floor - 1
    else:
        print("Error: unknown character.")

print(floor)