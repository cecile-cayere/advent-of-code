import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-08/input.txt')
content = split_string(content, "\n")

code_count = 0
memory_count = 0

for string in content:
    code_count = code_count + len(string)
    i = 0
    while i < len(string):
        if i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '\\':
            memory_count = memory_count + 1
            i = i + 2
            continue
        elif i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '"':
            memory_count = memory_count + 1
            i = i + 2
            continue
        elif string[i] == '"':
            i = i + 1
            continue
        elif i < len(string) - 3 and string[i] == '\\' and string[i + 1] == 'x' and is_hex(string[i + 2]) and is_hex(string[i + 3]):
            memory_count = memory_count + 1
            i = i + 4
            continue
        else:
            memory_count = memory_count + 1
            i = i + 1
            continue

print(code_count - memory_count)
