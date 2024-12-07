import sys
sys.path.append('../advent-of-code')
from utils import *
import os
import time

content = get_file_content('2024/day-07/input.txt')
content = split_string(content, "\n")

operators = []
results = []

for line in content:
    line = split_string(line, ": ")
    results.append(int(line[0]))
    operators.append(list(map(lambda n: int(n), split_string(line[1], " "))))

i = 0
sum = 0

for result in results:
    j = 0
    found = False
    possibilities = get_all_binary_numbers(len(operators[i]) - 1)

    while not found and j < len(possibilities):
        tmp_result = operators[i][0]
        k = 1
        for sign in possibilities[j]:
            if(sign == 0):
                tmp_result = tmp_result + operators[i][k]
            elif(sign == 1):
                tmp_result = tmp_result * operators[i][k]

            k = k + 1

        if(tmp_result == result):
            found = True
            sum = sum + result

        j = j + 1
    i = i + 1

print(sum)