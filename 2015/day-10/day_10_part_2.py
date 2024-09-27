import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-10/input.txt')

def look_and_say(sequence):
    if(len(sequence) == 0): return ""
    new_sequence = ""
    current_char = sequence[0]
    counter = 1
    i = 1

    while i < len(sequence):
        if(sequence[i] == current_char):
            counter = counter + 1
        else:
            new_sequence = new_sequence + str(counter) + current_char
            current_char = sequence[i]
            counter = 1
        if(i == len(sequence) - 1):
            new_sequence = new_sequence + str(counter) + current_char

        i = i + 1
    return new_sequence

sequence = str(content)
i = 0
while i < 50:
    print(i)
    sequence = look_and_say(sequence)
    i = i + 1

print(len(sequence))