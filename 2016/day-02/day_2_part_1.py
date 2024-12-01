import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2016/day-02/input.txt')
content = split_string(content, "\n")

keypad = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

current_button = [1, 1]
code = ""

for instructions in content:
    for instruction in instructions:
        if(instruction == "U"):
            if(current_button[0] > 0):
                current_button[0] = current_button[0] - 1
        elif(instruction == "D"):
            if(current_button[0] < 2):
                current_button[0] = current_button[0] + 1
        elif(instruction == "L"):
            if(current_button[1] > 0):
                current_button[1] = current_button[1] - 1
        elif(instruction == "R"):
            if(current_button[1] < 2):
                current_button[1] = current_button[1] + 1
        else:
            print("Error!")

    code = code + str(keypad[current_button[0]][current_button[1]])

print(code)