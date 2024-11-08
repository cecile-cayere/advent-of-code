import sys
import copy
sys.path.append('../advent-of-code')
from utils import *

x = int(get_file_content('2015/day-20/input.txt'))

def get_correct_house(x):
    houses = {}

    for i in range(1, x + 1):
        for j in range(i, x + 1, i):
            if(j in houses):
                houses[j] = houses[j] + (i * 10)
            else:
                houses[j] = (i * 10)

    i = 1
    for house in houses.values():
        if(house >= x):
            return(i)
        i += 1

print(get_correct_house(x))

# Other solution :
'''
house_number = 1
found = False
prime_nb = []

while not found:
    prime_factors = []
    nb_presents = 0

    if(house_number != 1 and is_prime(house_number)):
        prime_nb.append(house_number)
        nb_presents = nb_presents + (10 * house_number) + 10
    
    else:
        i = 0
        tmp = house_number

        while(tmp > 1):
            if(tmp % prime_nb[i] == 0):
                tmp = tmp / prime_nb[i]
                prime_factors.append(prime_nb[i])
            else: i += 1

        cases = get_binary_numbers(len(prime_factors))

        dividers = []
        for case in cases:
            j = 0
            nb = 1
            while j < len(case):
                if(case[j] == 1) :
                    nb = nb * prime_factors[j]
                j += 1
            
            if(nb not in dividers):
                dividers.append(nb)
                nb_presents = nb_presents + (10 * nb)
        

    if(nb_presents >= x): 
        found = True
        break
    
    house_number += 1

print(house_number)
'''