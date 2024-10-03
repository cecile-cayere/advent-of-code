import sys
sys.path.append('../advent-of-code')
from utils import *

json = get_file_content('2015/day-12/input.json')
current_number = ""
minus = False
sum = 0
i = 0
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


while i < len(json):
    if(current_number == "" and json[i] == "-"):
        minus = True

    elif(json[i] in numbers):
        current_number = current_number + json[i]

    elif(current_number != ""):
        if(minus == True): sum = sum + int("-" + current_number)
        else: sum = sum + int(current_number)

        minus = False
        current_number = ""

    i = i + 1

print(sum)

