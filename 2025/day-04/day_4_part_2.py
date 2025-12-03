import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-03/input.txt')
content = split_string(content, "\n")

total_joltage = 0
for bank in content:
    bank_table = list(map(int, list(bank)))
    joltage = ""

    for i in range(0, 12):
        end_index = len(bank_table) - (11 - i)
        tmp_bank_table = bank_table[:end_index]

        max_nb = max(tmp_bank_table)
        index_max_nb = tmp_bank_table.index(max_nb)
        bank_table = bank_table[index_max_nb+1:]
        
        joltage = joltage + str(max_nb)

    total_joltage = total_joltage + int(joltage)

print(total_joltage)