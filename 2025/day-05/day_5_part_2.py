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
        ranges.append([range_items[0].zfill(15), range_items[1].zfill(15)])
    else:
        products.append(line)

ranges = sorted(ranges, key=lambda x: x[0])

i = 0
while i < len(ranges) - 1:
    result = compare_big_numbers(ranges[i][1], ranges[i + 1][0])
    if(result == 1 or result == 0):
        if(ranges[i][1] < ranges[i + 1][1]):
            ranges[i][1] = ranges[i + 1][1]
        del ranges[i + 1]
    else:
        i = i + 1

count = 0
for range_item in ranges:
    range_start = int(range_item[0])
    range_end = int(range_item[1])
    count = count + (range_end - range_start) + 1

print(count)