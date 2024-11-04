import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-16/input.txt')
content = split_string(content, "\n")

aunt_sue = {"children": 3,
            "cats": 7, # > 7
            "samoyeds": 2,
            "pomeranians": 3, # < 3
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5, # < 5
            "trees": 3, # > 3
            "cars": 2,
            "perfumes": 1}

aunts_data = {}
aunts = []

for line in content:
    name = split_string(line, ": ")
    name = split_string(name[0], " ")[1]
    aunts_data[name] = {}
    aunts.append(name)

    features = split_string(line.replace(': ', '//', 1), "//")[1]
    features = split_string(features, ", ")

    for item in features:
        feature = split_string(item, ": ")
        aunts_data[name][feature[0]] = int(feature[1])

for aunt_key, aunt_value in aunts_data.items():
    for key, value in aunt_value.items():
        if(key in aunt_sue):
            if((key == "cats" or key == "trees") and int(aunt_sue[key]) >= int(value)) or ((key == "pomeranians" or key == "goldfish") and int(aunt_sue[key]) <= int(value)) or ((key not in ["cats", "trees", "pomeranians", "goldfish"]) and aunt_sue[key] != value):
                aunts.remove(aunt_key)
                break

print(int(aunts[0]))