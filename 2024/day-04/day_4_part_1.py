import sys
sys.path.append('../advent-of-code')
from utils import *
import re

content = get_file_content('2024/day-04/input.txt')
content = split_string(content, "\n")

word_search = init_2_dim_list(len(content), len(content[0]))

i = 0
for line in content:
    j = 0
    for char in line:
        word_search[i][j] = char
        j = j + 1
    i = i + 1

count = 0
i = 0
while i < len(word_search):
    j = 0
    while j < len(word_search[i]):
        if(word_search[i][j] == "X"):
            if(i < len(word_search) - 3 and word_search[i + 1][j] == "M" and word_search[i + 2][j] == "A" and word_search[i + 3][j] == "S"):
                count = count + 1
            if(i > 2 and word_search[i - 1][j] == "M" and word_search[i - 2][j] == "A" and word_search[i - 3][j] == "S"):
                count = count + 1
            if(j < len(word_search[i]) - 3 and word_search[i][j + 1] == "M" and word_search[i][j + 2] == "A" and word_search[i][j + 3] == "S"):
                count = count + 1
            if(j > 2 and word_search[i][j - 1] == "M" and word_search[i][j - 2] == "A" and word_search[i][j - 3] == "S"):
                count = count + 1
            if(i < len(word_search) - 3 and j < len(word_search[i]) - 3 and word_search[i + 1][j + 1] == "M" and word_search[i + 2][j + 2] == "A" and word_search[i + 3][j + 3] == "S"):
                count = count + 1
            if(i > 2 and j > 2 and word_search[i - 1][j - 1] == "M" and word_search[i - 2][j - 2] == "A" and word_search[i - 3][j - 3] == "S"):
                count = count + 1
            if(i < len(word_search) - 3 and j > 2 and word_search[i + 1][j - 1] == "M" and word_search[i + 2][j - 2] == "A" and word_search[i + 3][j - 3] == "S"):
                count = count + 1
            if(i > 2 and j < len(word_search[i]) - 3 and word_search[i - 1][j + 1] == "M" and word_search[i - 2][j + 2] == "A" and word_search[i - 3][j + 3] == "S"):
                count = count + 1
        j = j + 1
    i = i + 1

print(count)

