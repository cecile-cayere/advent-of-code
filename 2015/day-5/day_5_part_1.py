import sys
sys.path.append('../advent-of-code')
from utils import *

import hashlib

content = get_file_content('2015/day-5/input.txt')
content = split_string(content, "\n")

nice_strings = 0

for string in content:
    vowels = string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')
    if(vowels >= 3):
        if 'ab' not in string and 'cd' not in string and 'pq' not in string and 'xy' not in string:
            i = 0
            previous_letter = -1
            while i < len(string):
                if(previous_letter != -1 and previous_letter == string[i]):
                    nice_strings = nice_strings + 1
                    break
                previous_letter = string[i]
                i = i + 1

print(nice_strings)
