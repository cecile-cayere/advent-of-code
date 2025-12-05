import json

# Files:

def get_file_content(filename):
    with open(filename) as file:
        content = file.read()
        return content
    
def get_json_file_content(filename):
    with open(filename, 'r') as file:
        content = json.load(file)
        return content
    
def print_file_content(filename):
    with open(filename) as file:
        print(file.read())

def split_string(string, split_char):
    return(string.split(split_char))

# Dictionaries:

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(key, ": ", value)

def print_map(map):
    for line in map:
        for point in line:
            print(point, end=' ')
        print()

def in_map(map, coordinates):
    if(coordinates[0] >= 0 and coordinates[0] < len(map) and coordinates[1] >= 0 and coordinates[1] < len(map[coordinates[0]])):
        return(True)
    else:
        return(False)


# Bits:

def get_all_binary_numbers(size):
    lst = []

    for i in range(1 << size):
        binary_nb = bin(i)[2:]
        binary_nb = '0' * (size - len(binary_nb)) + binary_nb
        lst = lst + [list(map(int, list(binary_nb)))]

    return(lst)

def pad_bits(bit_table, length = 16):
    return [0]*(length - len(bit_table)) + bit_table

def convert_int_to_bits(decimal_nb):
    quotient = decimal_nb // 2
    remainder = decimal_nb % 2
    if(quotient == 0):
        return [remainder]
    return convert_int_to_bits(decimal_nb // 2) + [remainder]
    
def convert_bits_to_int(bits_table):
    result = 0
    i = len(bits_table) - 1
    while(i >= 0):
        result = result + (bits_table[i] * (2 ** (len(bits_table) - 1 - i)))
        i = i - 1
    return result

def and_bits(bits_table_a, bits_table_b):
    result = []
    i = len(bits_table_a) - 1
    while(i >= 0):
        result.append(bits_table_a[i] & bits_table_b[i])
        i = i - 1
    return result[::-1]

def or_bits(bits_table_a, bits_table_b):
    result = []
    i = len(bits_table_a) - 1
    while(i >= 0):
        result.append(bits_table_a[i] | bits_table_b[i])
        i = i - 1
    return result[::-1]

def not_bits(bits_table):
    result = []
    i = len(bits_table) - 1
    while(i >= 0):
        if(bits_table[i] == 1): result.append(0)
        else: result.append(1)
        i = i - 1
    return result[::-1]

def lshift_bits(bits_table, shift):
    result = bits_table[:]

    while(shift > 0):
        i = 1
        while(i < len(bits_table)):
            result[i - 1] = result[i]
            i = i + 1
        result[len(bits_table) - 1] = 0
        shift = shift - 1

    return result

def rshift_bits(bits_table, shift):
    result = bits_table[:]

    while(shift > 0):
        i = len(bits_table) - 2
        while(i >= 0):
            result[i + 1] = result[i]
            i = i - 1
        result[0] = 0
        shift = shift - 1
        
    return result


# Numbers

def get_sign(x):
    if(x != 0):
        return(x / abs(x))
    else:
        return(1)
    
def is_prime(x):
    if x == 0 or x == 1:
        return False
    elif x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                return False
        return True

def is_hex(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False

# Points

def get_distance_between_points(point_1, point_2):
    return(abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1]))


# Lists:

def init_1_dim_list(x):
    return([0] * x)

def init_2_dim_list(x, y):
    return([[0] * x for i in range(y)])

def count_values_in_2_dim_list(lst, value):
    return(sum(row.count(value) for row in lst))

def sum_values_in_2_dim_list(lst):
    return(sum(sum(row) for row in lst))

def get_max_from_list(lst):
    return max(lst)

def get_min_from_list(lst):
    return max(lst)

def remove_all_x_values_from_list(lst, x):
   return [value for value in lst if value != x]

def remove_one_x_value_from_list(lst, x):
    lst.remove(x)
    return(lst)

def get_list_sum(lst):
    return(sum(lst))

def swap_item_in_lst(lst, i, j):
    lst = list(lst)
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def permute_lst(lst, index):
    result = []
    if index == len(lst) - 1:
        return [lst]
    
    for i in range(index, len(lst)):
        lst = swap_item_in_lst(lst, index, i)

        result = result + permute_lst(lst, index + 1)

        lst = swap_item_in_lst(lst, index, i)

    return result

# Triangles:

def is_segments_triangle(segments):
    max = get_max_from_list(segments)
    list_without_max = remove_one_x_value_from_list(segments, max)

    if(get_list_sum(list_without_max) > max):
        return(True)
    else:
        return(False)



def compare_big_numbers(a: str, b: str) -> int:
    # Suppression des zéros en tête :
    a = a.lstrip('0')
    b = b.lstrip('0')

    # 1. Comparaison des longueurs :
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1

    # 2. Comparaison lexicographique :
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0