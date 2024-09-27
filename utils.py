# Files:
def get_file_content(filename):
    with open(filename) as file:
        content = file.read()
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


# Lists:
def init_1_dim_list(x):
    return([0]*x)

def init_2_dim_list(x, y):
    return([[0]*x for i in range(y)])

def count_values_in_2_dim_list(list, value):
    return(sum(row.count(value) for row in list))

def sum_values_in_2_dim_list(list):
    return(sum(sum(row) for row in list))

# Bits:

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

def is_hex(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False

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