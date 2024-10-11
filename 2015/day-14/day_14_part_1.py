import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-14/input.txt')
content = split_string(content, "\n")

reindeers = {}
olympics = {}
    
for line in content:
    line = split_string(line, " can fly ")
    reindeer = line[0]
    line = split_string(line[1], " km/s for ")
    km_s = int(line[0])
    line = split_string(line[1], " seconds, but then must rest for ")
    move_time = int(line[0])
    rest_time = int(split_string(line[1], " seconds.")[0])

    reindeers[reindeer] = [km_s, move_time, rest_time, 0, move_time, 0]
  
i = 0

while i < 2503:
    for reindeer in reindeers.values():
        if(reindeer[4] > 0):
            reindeer[3] = reindeer[3] + reindeer[0]
            reindeer[4] = reindeer[4] - 1

            if(reindeer[4] == 0):
                reindeer[5] = reindeer[2]
        
        elif(reindeer[5] > 0):
            reindeer[5] = reindeer[5] - 1

            if(reindeer[5] == 0):
                reindeer[4] = reindeer[1]
    i = i + 1

distance = 0
for reindeer in reindeers.values():
    if(reindeer[3] > distance):
        distance = reindeer[3]

print(distance)