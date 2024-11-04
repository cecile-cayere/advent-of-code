import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-17/input.txt')
content = split_string(content, "\n")
containers = []

for line in content:
    containers.append(int(line))

containers.sort()
possibilities = 0

for i in range(1 << len(containers)):
    s = bin(i)[2:]
    s = '0' * (len(containers) - len(s)) + s
    s = list(map(int, list(s)))

    total = 0
    j = 0
    while j < len(s):
        if(s[j] == 1):
            total = total + containers[j]
            if(total > 150):
                break
        j = j + 1
    
    if(total == 150):
        possibilities = possibilities + 1

print(possibilities)