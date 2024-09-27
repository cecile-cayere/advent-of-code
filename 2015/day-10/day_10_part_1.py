import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-10/input.txt')

def look_and_say(sequence, iter):
    print(iter)
    sequence = str(sequence)
    if(len(sequence) == 0): return ""
    if(iter == 0): return sequence

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

    return look_and_say(new_sequence, iter - 1)


print(len(look_and_say(content, 50)))