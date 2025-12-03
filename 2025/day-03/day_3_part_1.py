import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-03/input.txt')
content = split_string(content, "\n")

total_joltage = 0
for bank in content:
    joltage = 0
    current_joltage = ""
    for index1 in range(0, len(bank)):
        for index2 in range(index1 + 1, len(bank)):
            current_joltage = str(bank[index1]) + (bank[index2])
            if(int(current_joltage) > joltage):
                joltage = int(current_joltage)
    total_joltage = total_joltage + joltage

print(total_joltage)