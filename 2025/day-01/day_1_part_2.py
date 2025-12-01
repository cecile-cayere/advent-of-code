import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-01/input.txt')
content = split_string(content, "\n")

pointing_at = 50
count = 0

for instruction in content:
    direction = instruction[0]
    clics_nb = int(instruction[1:])

    if(direction == "R"):
        count = count + ((pointing_at + clics_nb) // 100)
        pointing_at = (pointing_at + clics_nb) % 100
    elif(direction == "L"):
        count = count + abs((pointing_at - clics_nb) // 100)
        pointing_at = (pointing_at - clics_nb) % 100
    else:
        print("Error")

print(count)