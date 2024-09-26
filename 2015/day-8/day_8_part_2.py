import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-8/input.txt')
content = split_string(content, "\n")

code_count = 0
encode_count = 0

for string in content:
    code_count = code_count + len(string)
    i = 0
    encode_count = encode_count + 2
    while i < len(string):
        if i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '\\':
            encode_count = encode_count + 4
            i = i + 2
            continue
        elif i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '"':
            encode_count = encode_count + 4
            i = i + 2
            continue
        elif string[i] == '"':
            encode_count = encode_count + 2
            i = i + 1
            continue
        elif i < len(string) - 3 and string[i] == '\\' and string[i + 1] == 'x' and is_hex(string[i + 2]) and is_hex(string[i + 3]):
            encode_count = encode_count + 5
            i = i + 4
            continue
        else:
            encode_count = encode_count + 1
            i = i + 1
            continue

print(encode_count - code_count)
