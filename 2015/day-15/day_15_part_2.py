import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-15/input.txt')
content = split_string(content, "\n")

def decimal_to_hundred(decimal):
    result = []
    quotient = decimal

    while quotient != 0:
        remainder = quotient % 101
        quotient = quotient // 101

        result = [remainder] + result

    while(len(result) < 4):
        result = [0] + result

    return result

def hundred_to_decimal(hundred):
    result = 0
    i = 0
    
    while i < len(hundred):
        result = result + (hundred[i] * (101 ** (len(hundred) - i - 1)))
        i = i + 1

    return result

specification = []
    
for line in content:
    line = split_string(line, ": ")
    name = line[0]
    line = split_string(line[1], ", ")

    specification.append([int(split_string(line[0], " ")[1]), 
                        int(split_string(line[1], " ")[1]), 
                        int(split_string(line[2], " ")[1]), 
                        int(split_string(line[3], " ")[1]), 
                        int(split_string(line[4], " ")[1])])

quantity = [0, 0, 0, 0]
conv_quantity = hundred_to_decimal(quantity)
best_score = 0

while quantity != [100, 0, 0, 0]:
    conv_quantity = conv_quantity + 1
    quantity = decimal_to_hundred(conv_quantity)

    if(sum(quantity) == 100):
        calories =      quantity[0] * specification[0][4] + quantity[1] * specification[1][4] + quantity[2] * specification[2][4] + quantity[3] * specification[3][4]
        
        if(calories == 500):
            capacity =      quantity[0] * specification[0][0] + quantity[1] * specification[1][0] + quantity[2] * specification[2][0] + quantity[3] * specification[3][0]
            durability =    quantity[0] * specification[0][1] + quantity[1] * specification[1][1] + quantity[2] * specification[2][1] + quantity[3] * specification[3][1]
            flavor =        quantity[0] * specification[0][2] + quantity[1] * specification[1][2] + quantity[2] * specification[2][2] + quantity[3] * specification[3][2]
            texture =       quantity[0] * specification[0][3] + quantity[1] * specification[1][3] + quantity[2] * specification[2][3] + quantity[3] * specification[3][3]
            
            if(capacity < 0): capacity = 0
            if(durability < 0): durability = 0
            if(flavor < 0): flavor = 0
            if(texture < 0): texture = 0

            score = capacity * durability * flavor * texture
            if(score > best_score):
                best_score = score
            
print(best_score)