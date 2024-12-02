import sys
sys.path.append('../advent-of-code')
from utils import *
import math

content = get_file_content('2024/day-02/input.txt')
content = split_string(content, "\n")

def is_safe(report):
    previous_level = -1
    previous_way = 0

    for level in report:
        if(previous_level != -1):
            space = previous_level - level
            way = get_sign(space)

            if(previous_level == level):
                return(False)

            if(previous_way != 0 and way != previous_way):
                return(False)

            if(space > 3 or space < -3):
                return(False)

            previous_way = way
        previous_level = level
        
    return(True)

reports = []

for line in content:
    line = split_string(line, " ")
    report = []

    for number in line:
        report.append(int(number))

    reports.append(report)

safe = 0

for report in reports:
    if(is_safe(report)):
        safe = safe + 1

print(safe)