import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2024/day-09/input.txt')

blocs = []

i = 0
j = 0
while i < len(content):
    if(int(content[i]) != 0):
        if(i % 2 == 0):
            blocs.append([int(content[i]), j])
            j = j + 1
        else:
            blocs.append([int(content[i]), -1])
    i = i + 1

i = 0
while i < len(blocs):
    if(blocs[i][1] == -1):
        j = len(blocs) - 1
        while(j >= 0 and blocs[j][1] == -1):
            j = j - 1

        if(blocs[i][0] == blocs[j][0]):
            blocs[i][1] = blocs[j][1]
            blocs[j][1] = -1
        elif(blocs[i][0] > blocs[j][0]):
            blocs[i][0] = blocs[i][0] - blocs[j][0]
            tmp = list(blocs[j])
            del blocs[j]
            blocs.insert(i, tmp)
        elif(blocs[i][0] < blocs[j][0]):
            blocs[j][0] = blocs[j][0] - blocs[i][0]
            blocs[i][1] = blocs[j][1]
            i = i + 1

    else:
        i = i + 1

checksum = 0

i = 0
for bloc in blocs:
    j = 0
    while j < bloc[0]:
        if(bloc[1] != -1):
            checksum = checksum + (i * bloc[1])
            i = i + 1
        j = j + 1

print(checksum)