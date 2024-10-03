import sys
sys.path.append('../advent-of-code')
from utils import *

json_content = get_json_file_content('2015/day-12/input.json')

def browse_json(json):
    sum = 0
    if(type(json) == list):
        for i in json:
            sum = sum + browse_json(i)
        return sum

    elif(type(json) == dict):
        if "red" not in json and 'red' not in json.values():
            for i in json:
                sum = sum + browse_json(json[i])
            return sum
        return 0

    else:
        try:
            return(int(json))
                   
        except ValueError:
            return 0

print(browse_json(json_content))