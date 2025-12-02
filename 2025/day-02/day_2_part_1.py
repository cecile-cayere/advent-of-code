import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-02/input.txt')
content = split_string(content, ",")

sum = 0

for range in content:
    ids = split_string(range, "-")
    id_start = ids[0]
    id_end = ids[1]

    while int(id_start) != int(id_end) + 1:
        middle_index = int(len(id_start) / 2)
        if(len(id_start) % 2 == 0 and id_start[:middle_index] == id_start[middle_index:]):
            print(id_start)
            sum = sum + int(id_start)
        id_start = str(int(id_start) + 1)
        

print(sum)