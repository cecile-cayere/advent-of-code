import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-02/input.txt')
content = split_string(content, ",")
sum = 0

for range in content:
    ids = split_string(range, "-")
    id_start = ids[0]
    id_end = ids[1]
    
    # Boucle pour parcourir les ids :
    while int(id_start) <= int(id_end) + 1:
        spliter = 2
        find_invalid_id = False

        # Boucle pour chager la taille du spliter :
        while not find_invalid_id and spliter <= len(id_end) :
            if len(id_start) % spliter == 0:
                index = int(len(id_start) / spliter)
                model = id_start[:index]
                rest = id_start
                invalid_id = True

                # Boucle pour comparer les parties de l'id :
                while invalid_id and len(rest) >= len(model):
                    current_part = rest[:index]
                    if(current_part != model):
                        invalid_id = False
                    rest = rest[index:]

                if(invalid_id):
                    find_invalid_id = True
                    sum = sum + int(id_start)
            spliter = spliter + 1
        id_start = str(int(id_start) + 1)

print(sum)