import sys
sys.path.append('../advent-of-code')
from utils import *
import copy
import math

content = get_file_content('2015/day-25/input.txt')
content = split_string(split_string(content, "To continue, please consult the code grid in the manual.  Enter the code at row ")[1], ", column ")
code_row = int(content[0])
code_column = int(split_string(content[1], ".")[0]) 
print(code_row)
print(code_column)

def coord_to_key_num(row, column):
    return(int((((row + column - 1) * (row + column)) / 2) - (row - 1)))

key_num = coord_to_key_num(code_row, code_column)
code = 20151125

for i in range(key_num - 1):
    code = (code * 252533) % 33554393

print(code)