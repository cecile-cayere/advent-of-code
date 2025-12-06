import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-06/input.txt')
content = split_string(content, "\n")

sheet = []
i = 0
for line in content:
    sheet.append([])
    for char in line:
        sheet[i].append(char)
    i = i + 1

sum = 0
i = 0
result = -1
operator = ""

while i < len(sheet[0]):
    if(sheet[-1][i] == "+"):
        if result > 0:
            sum = sum + result
        operator = "+"
        result = 0
    elif(sheet[-1][i] == "*"):
        if result > 1:
            sum = sum + result
        operator = "*"
        result = 1

    tmp = ""
    j = 0
    while j < len(sheet) - 1:
        tmp = tmp + sheet[j][i]
        j = j + 1
    tmp = tmp.strip()

    if(tmp != ""):
        if(operator == "+"):
            result = result + int(tmp)
        else:
            result = result * int(tmp)

    i = i + 1

if result > 0:
    sum = sum + result

print(sum)