import sys
sys.path.append('../advent-of-code')
from utils import *

import hashlib

key = get_file_content('2015/day-04/input.txt')

found = False
i = 0

while not found:
    input = key + str(i)
    hashes = hashlib.md5(input.encode())
    if(hashes.hexdigest().startswith("00000")):
        found = True
    else:
        i = i + 1

print(i)
