import sys
sys.path.append('../advent-of-code')
from utils import *

summits = []

content = get_file_content('2024/day-11/input.txt')
content = split_string(content, " ")

stones = []

for char in content:
    stones.append(char)

i = 25

while i > 0:
    new_stones = list(stones)
    j = 0
    k = 0
    for stone in stones:
        if(stone == "0"):
            new_stones[k] = "1"
        elif(len(stone) % 2 == 0):
            half = int(len(stone)/2)
            new_stones[k] = str(int(stones[j][half:]))
            new_stones.insert(k, str(int(stones[j][:half])))
            k = k + 1
        else:
            new_stones[k] = str(int(stones[j]) * 2024)

        j = j + 1
        k = k + 1

    stones = new_stones
    i = i - 1

print(len(stones))