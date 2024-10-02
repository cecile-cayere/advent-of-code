import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-11/input.txt')

def is_psw_valid(psw):
    check_sequence = False
    check_invalid_letters = True
    nb_pairs = 0
    previous_pair = 0
    i = 0

    while i < len(psw):
        if(i < len(psw) - 2 and ord(psw[i]) + 1 == ord(psw[i + 1]) and ord(psw[i + 1]) + 1 == ord(psw[i + 2])):
            check_sequence = True

        if(psw[i] == "i" or psw[i] == "o" or psw[i] == "l"):
            check_invalid_letters = False
        
        if(previous_pair != i - 1 and i < len(psw) - 1 and psw[i] == psw[i + 1]):
            previous_pair = i
            nb_pairs = nb_pairs + 1

        i = i + 1
    
    return check_sequence and check_invalid_letters and nb_pairs > 1

def decimal_to_alpha(decimal):
    result = ""
    quotient = decimal

    while quotient != 0:
        remainder = quotient % 26
        quotient = quotient // 26

        result = chr(remainder + 97) + result

    return result

def alpha_to_decimal(alpha):
    result = 0
    i = 0
    
    while i < len(alpha):
        result = result + ((ord(alpha[i]) - 97) * (26 ** (len(alpha) - i - 1)))
        i = i + 1

    return result

new_psw = content
conv_psw = alpha_to_decimal(new_psw)

is_valid = False

while not is_valid:
    conv_psw = conv_psw + 1
    new_psw = decimal_to_alpha(conv_psw)

    if(is_psw_valid(new_psw)):
        is_valid = True

print(new_psw)

