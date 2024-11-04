import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-07/input.txt')
content = split_string(content, "\n")

wires_off = {}
wires_on = {}

for instruction in content:
    value, result = split_string(instruction, " -> ")
    
    if value.isnumeric(): wires_on[result] = pad_bits(convert_int_to_bits(int(value)))
    else: wires_off[result] = value

while len(wires_off) > 0:
    for key, value in wires_off.copy().items():
        if "NOT " in value:
            wire = split_string(value, "NOT ")[1]

            if wire in wires_on: 
                wires_on[key] = not_bits(wires_on[wire])
                del wires_off[key]
            elif wire.isnumeric():
                wires_on[key] = not_bits(pad_bits(convert_int_to_bits(int(wire))))
                del wires_off[key]
        
        elif " AND " in value:
            wire_a, wire_b = split_string(value, " AND ")
            if wire_a in wires_on and wire_b in wires_on: 
                wires_on[key] = and_bits(wires_on[wire_a], wires_on[wire_b])
                del wires_off[key]
            elif wire_a.isnumeric() and wire_b in wires_on: 
                wires_on[key] = and_bits(pad_bits(convert_int_to_bits(int(wire_a))), wires_on[wire_b])
                del wires_off[key]
            elif wire_a in wires_on and wire_b.isnumeric(): 
                wires_on[key] = and_bits(wires_on[wire_a], pad_bits(convert_int_to_bits(int(wire_b))))
                del wires_off[key]
            elif wire_a.isnumeric() and wire_b.isnumeric(): 
                wires_on[key] = and_bits(pad_bits(convert_int_to_bits(int(wire_a))), pad_bits(convert_int_to_bits(int(wire_b))))
                del wires_off[key]
            
        elif " OR " in value:
            wire_a, wire_b = split_string(value, " OR ")
            if wire_a in wires_on and wire_b in wires_on: 
                wires_on[key] = or_bits(wires_on[wire_a], wires_on[wire_b])
                del wires_off[key]
            elif wire_a.isnumeric() and wire_b in wires_on: 
                wires_on[key] = or_bits(pad_bits(convert_int_to_bits(int(wire_a))), wires_on[wire_b])
                del wires_off[key]
            elif wire_a in wires_on and wire_b.isnumeric():
                wires_on[key] = or_bits(wires_on[wire_a], pad_bits(convert_int_to_bits(int(wire_b))))
                del wires_off[key]
            elif wire_a.isnumeric() and wire_b.isnumeric(): 
                wires_on[key] = or_bits(pad_bits(convert_int_to_bits(int(wire_a))), pad_bits(convert_int_to_bits(int(wire_b))))
                del wires_off[key]

        if " LSHIFT " in value:
            wire, shift = split_string(value, " LSHIFT ")
            if wire in wires_on: 
                wires_on[key] = lshift_bits(wires_on[wire], int(shift))
                del wires_off[key]
            elif wire.isnumeric():
                wires_on[key] = lshift_bits(pad_bits(convert_int_to_bits(int(wire))), int(shift))
                del wires_off[key]

        elif " RSHIFT " in value:
            wire, shift = split_string(value, " RSHIFT ")
            if wire in wires_on: 
                wires_on[key] = rshift_bits(wires_on[wire], int(shift))
                del wires_off[key]
            elif wire.isnumeric():
                wires_on[key] = rshift_bits(pad_bits(convert_int_to_bits(int(wire))), int(shift))
                del wires_off[key]
        
        else:
            if value in wires_on: 
                wires_on[key] = wires_on[value]
                del wires_off[key]

if 'a' in wires_on: print(convert_bits_to_int(wires_on['a']))