import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2024/day-11/input.txt')
content = split_string(content, " ")

stones = {}

for char in content:
    if(int(char) in stones):
        stones[int(char)] = stones[int(char)] + 1
    else:
        stones[int(char)] = 1

i = 75

while i > 0:
    new_stones = {}
    for stone, count in stones.items():
        if stone == 0:
            if(1 in new_stones):
                new_stones[1] += count
            else:
                new_stones[1] = count
        else:
            str_stone = str(stone)
            if len(str_stone) % 2 == 0:
                half = len(str_stone) // 2
                left = int(str_stone[:half])
                right = int(str_stone[half:])

                if(left in new_stones):
                    new_stones[left] += count
                else:
                    new_stones[left] = count

                if(right in new_stones):
                    new_stones[right] += count
                else:
                    new_stones[right] = count
            else:
                key = stone * 2024
                if(key in new_stones):
                    new_stones[key] += count
                else:
                    new_stones[key] = count

    stones = new_stones
    i -= 1

print(sum(stones.values()))