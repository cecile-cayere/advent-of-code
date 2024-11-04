import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-03/input.txt')

map = {
  "0;0": 2
}

current_santa_pos = "0;0"
current_robo_pos = "0;0"
i = 1

for char in content:
    # Santa turn :
    if(i % 2 == 1):
        split = split_string(current_santa_pos, ";")

        if(char == ">"):
            current_santa_pos = split[0] + ";" + str(int(split[1]) + 1)
        elif(char == "v"):
            current_santa_pos = str(int(split[0]) + 1) + ";" + split[1]
        elif(char == "<"):
            current_santa_pos = split[0] + ";" + str(int(split[1]) - 1)
        elif(char == "^"):
            current_santa_pos = str(int(split[0]) - 1) + ";" + split[1]
        else:
            print("Error: unknown character.")
            
        if current_santa_pos in map:
            map[current_santa_pos] = map[current_santa_pos] + 1
        else: 
            map[current_santa_pos] = 1

    # Robo-Santa turn :
    elif(i % 2 == 0):
        split = split_string(current_robo_pos, ";")

        if(char == ">"):
            current_robo_pos = split[0] + ";" + str(int(split[1]) + 1)
        elif(char == "v"):
            current_robo_pos = str(int(split[0]) + 1) + ";" + split[1]
        elif(char == "<"):
            current_robo_pos = split[0] + ";" + str(int(split[1]) - 1)
        elif(char == "^"):
            current_robo_pos = str(int(split[0]) - 1) + ";" + split[1]
        else:
            print("Error: unknown character.")

        if current_robo_pos in map:
            map[current_robo_pos] = map[current_robo_pos] + 1
        else: 
            map[current_robo_pos] = 1

    else:
        print("Error: unknown turn.")

    i = i + 1

print(len(map))