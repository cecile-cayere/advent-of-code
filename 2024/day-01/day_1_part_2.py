import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2024/day-01/input.txt')
content = split_string(content, "\n")

lst_1 = []
lst_2 = []

for line in content:
    item_1, item_2 = split_string(line, "   ")
    lst_1.append(int(item_1))
    lst_2.append(int(item_2))
    
lst_1.sort()
lst_2.sort()

i = 0
sum = 0
while i < len(lst_1):
    sum = sum + (lst_1[i] * lst_2.count(lst_1[i]))
    i = i + 1

print(sum)