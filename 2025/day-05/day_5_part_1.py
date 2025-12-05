import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-05/input.txt')
content = split_string(content, "\n")

ranges = []
products = []
for line in content:
    line = line.strip()
    if line == "":
        pass
    elif("-" in line):
        range_items = split_string(line, "-")
        ranges.append([range_items[0], range_items[1]])
    else:
        products.append(line)

count = 0
for product in products:
    found_range = False
    i = 0
    while not found_range and i < len(ranges):
        result = compare_big_numbers(product, ranges[i][0])
        if(result == 1 or result == 0):
            result = compare_big_numbers(product, ranges[i][1])
            if(result == -1 or result == 0):
                found_range = True
                count = count + 1
        i = i + 1
print(count)
