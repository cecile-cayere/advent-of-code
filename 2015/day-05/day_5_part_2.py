import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-05/input.txt')
content = split_string(content, "\n")

nice_strings = 0

for string in content:
    i = 0
    check_1 = False
    check_2 = False
    
    while i < len(string) and (not check_1 or not check_2) :
        if(i + 1 < len(string)):
            if(i + 2 < len(string)):
                pair = string[i:i + 2]
                half_1 = string[0:i]
                half_2 = string[i + 2:]
            else:
                pair = string[i:]
                half_1 = string[0:i]
                half_2 = ""
            
            if(half_1.count(pair) >= 1 or half_2.count(pair) >= 1):
                check_1 = True
        
        if(i + 2 < len(string) and string[i] == string[i + 2]):
            check_2 = True

        i = i + 1
    
    if(check_1 and check_2):
        nice_strings = nice_strings + 1

print(nice_strings)
