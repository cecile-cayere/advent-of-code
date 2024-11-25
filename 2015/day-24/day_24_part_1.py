import sys
sys.path.append('../advent-of-code')
from utils import *
import copy
import math

content = get_file_content('2015/day-24/input.txt')
content = split_string(content, "\n")
packages = []

for line in content:
    packages.append(int(line))

max_weight = int(sum(packages) / 3)
groups = []

def filter_list_items_by_size(lst, size):
    new_lst = []
    for i in lst:
        if(len(i) == size):
            new_lst.append(i)
    return new_lst

def get_lst_minus_group(lst, group):
    new_lst = []
    for i in lst:
        if(i not in group):
            new_lst.append(i)
    return new_lst

def compute_groups(packages, group, size):
    global groups

    if(len(group) == size or (size == -1 and len(group) > 0)):
        if(sum(group) == max_weight):
            if(sorted(group) not in groups):
                groups.append(sorted(group))
            return -1 
        
        elif(sum(group) > max_weight):
            return -1 
    
    if(len(group) < size or size == -1):
        tmp_packages = copy.deepcopy(packages)
        for package in packages:
            tmp_group = copy.deepcopy(group)
            tmp_packages.remove(package)
            tmp_group.append(package)
            compute_groups(tmp_packages, tmp_group, size)
    
    else: return -1

i = 0
found = False
while i < len(packages) and not found:
    groups = []
    compute_groups(packages, [], i)

    if len(groups) > 0:
        sorted_groups = sorted(groups, key = lambda index : math.prod(index))

        for group in sorted_groups:
            packages_minus_group = get_lst_minus_group(packages, group)
            groups = []
            compute_groups(packages_minus_group, [], -1)

            if(len(groups) > 1):
                qe = math.prod(group)
                found = True
                break

    i = i + 1

print(qe)