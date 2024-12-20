import sys
import copy
sys.path.append('../advent-of-code')
from utils import *

x = int(get_file_content('2015/day-20/input.txt'))

def get_correct_house(x):
    houses = {}

    for i in range(1, x + 1):
        counter = 0
        for j in range(i, x + 1, i):
            if(counter == 50):
                break

            if(j in houses):
                houses[j] = houses[j] + (i * 11)
            else:
                houses[j] = (i * 11)
        
            counter += 1

            
    for key, house in houses.items():
        if(house >= x):
            return(key)

print(get_correct_house(x))

# Other solution :
'''
house_number = 1
found = False
prime_nb = []
elves = {}

while not found:
    prime_factors = []
    nb_presents = 0

    if(house_number != 1 and is_prime(house_number)):
        prime_nb.append(house_number)
        if(house_number not in elves):
            elves[house_number] = 1
            if(elves[1] < 50):
                nb_presents = nb_presents + (11 * house_number) + 11
                elves[1] = elves[1] + 1
            else:
                nb_presents = nb_presents + (11 * house_number)
        else:
            if(elves[1] < 50) and (elves[house_number] < 50):
                nb_presents = nb_presents + (11 * house_number) + 11
                elves[house_number] = elves[house_number] + 1
                elves[1] = elves[1] + 1
            elif(elves[house_number] < 50):
                nb_presents = nb_presents + (11 * house_number)
                elves[house_number] = elves[house_number] + 1
            elif(elves[1] < 50):
                nb_presents = nb_presents + 11
                elves[1] = elves[1] + 1
    
    else:
        i = 0
        tmp = house_number

        while(tmp > 1):
            if(tmp % prime_nb[i] == 0):
                tmp = tmp / prime_nb[i]
                prime_factors.append(prime_nb[i])
            else: i += 1

        cases = get_all_binary_numbers(len(prime_factors))

        dividers = []
        for case in cases:
            j = 0
            nb = 1
            while j < len(case):
                if(case[j] == 1) :
                    nb = nb * prime_factors[j]
                j += 1
            
            if(nb not in dividers):
                if(nb not in elves):
                    elves[nb] = 1
                    nb_presents = nb_presents + (11 * nb)
                    dividers.append(nb)
                elif(elves[nb] < 50):
                    elves[nb] = elves[nb] + 1
                    nb_presents = nb_presents + (11 * nb)
                    dividers.append(nb)
        

    if(nb_presents >= x): 
        found = True
        break

    house_number += 1

print(house_number)'''