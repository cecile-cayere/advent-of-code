import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-06/input.txt')
content = split_string(content, "\n")

sheet = []

for line in content:
    line = " ".join(line.split())
    sheet.append(split_string(line, " "))

length = len(sheet)
sum = 0
i = 0

while i < len(sheet[0]):
    if(sheet[-1][i] == "+"):
        result = 0
        j = 0
        while j < length - 1:
            result = result + int(sheet[j][i])
            j = j + 1
    else:
        result = 1
        j = 0
        while j < length - 1:
            result = result * int(sheet[j][i])
            j = j + 1
    sum = sum + result
    i = i + 1

print(sum)