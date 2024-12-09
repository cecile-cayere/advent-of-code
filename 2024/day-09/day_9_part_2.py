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
            index = j
            j = j + 1
        else:
            blocs.append([int(content[i]), -1])
    i = i + 1

while index >= 0:
    i = len(blocs) - 1
    while(i >= 0 and blocs[i][1] != index):
        i = i - 1

    j = 0
    has_moved = False
    while not has_moved and j < i:
        if(blocs[j][1] == -1):
            if(blocs[i][0] == blocs[j][0]):
                blocs[j][1] = blocs[i][1]

                if(i + 1 < len(blocs) and blocs[i - 1][1] == -1) and (blocs[i + 1][1] == -1):
                    blocs[i - 1][0] = blocs[i - 1][0] + blocs[i][0] + blocs[i + 1][0] 
                    del blocs[i:i + 2]
                elif(blocs[i - 1][1] == -1):
                    blocs[i - 1][0] = blocs[i - 1][0] + blocs[i][0]
                    del blocs[i]
                elif(i + 1 < len(blocs) and blocs[i + 1][1] == -1):
                    blocs[i][0] = blocs[i][0] + blocs[i + 1][0]
                    blocs[i][1] = -1
                    del blocs[i + 1]
                else:
                    blocs[i][1] = -1

                has_moved = True

            elif(blocs[j][0] > blocs[i][0]):
                blocs[j][0] = blocs[j][0] - blocs[i][0]
                tmp = list(blocs[i])

                if(i + 1 < len(blocs) and blocs[i - 1][1] == -1) and (blocs[i + 1][1] == -1):
                    blocs[i - 1][0] = blocs[i - 1][0] + blocs[i][0] + blocs[i + 1][0] 
                    del blocs[i:i + 2]
                elif(blocs[i - 1][1] == -1):
                    blocs[i - 1][0] = blocs[i - 1][0] + blocs[i][0]
                    del blocs[i]
                elif(i + 1 < len(blocs) and blocs[i + 1][1] == -1):
                    blocs[i][0] = blocs[i][0] + blocs[i + 1][0]
                    blocs[i][1] = -1
                    del blocs[i + 1]
                else:
                    blocs[i][1] = -1

                blocs.insert(j, tmp)

                has_moved = True
        j = j + 1
    index = index - 1
    
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