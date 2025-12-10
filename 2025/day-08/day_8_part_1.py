import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-08/input.txt')
content = split_string(content, "\n")

debug = False
junction_boxes = []

if(debug):
    print("Contruction du tableau de boîtes de jonctions.")
for line in content:
    junction_boxes.append(list(map(int, split_string(line, ","))))

distances = {}
i = 0

if(debug):
    print("Calcul des distances entre les boîtes de jonctions.")
for point_1 in junction_boxes:
    j = 0
    for point_2 in junction_boxes:
        if(point_1 != point_2 and (str(j) + "-" + str(i)) not in distances):
            distance = get_distance_between_3d_points(point_1, point_2)
            key = str(i) + "-" + str(j)
            distances[key] = distance
        j = j + 1
    i = i + 1

distances = dict(sorted(distances.items(), key=lambda item: item[1]))

pairs_nb = 1000
circuits  = [[i] for i in range(0, len(junction_boxes))]
i = 0

if(debug):
    print("Construction des circuits")
while i < pairs_nb and len(distances) > 0:
    first_distance = list(distances.items())[0]
    if(debug):
        print("Connection de la paire " + first_distance[0] + ".")
    indexes = split_string(first_distance[0], "-")
    index_1 = int(indexes[0])
    index_2 = int(indexes[1])
    value = first_distance[1]
    circuit_1 = None
    circuit_2 = None
    j = 0
    for circuit in circuits:
        if(index_1 in circuit):
            circuit_1 = j
        elif(index_2 in circuit):
            circuit_2 = j
        j = j + 1

    if(circuit_1 != None and circuit_2 != None):
        circuits[circuit_1] = circuits[circuit_1] + circuits[circuit_2]
        del circuits[circuit_2]

    del distances[first_distance[0]]
    i = i + 1

len_list = []

for circuit in circuits:
    len_list.append(len(circuit))

len_list = sorted(len_list, reverse=True)
if(len(len_list) >= 3):
    print(len_list[0] * len_list[1] * len_list[2])
elif(debug):
    print("Il y a moins de 3 circuits.")