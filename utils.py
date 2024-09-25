def get_file_content(filename):
    with open(filename) as file:
        content = file.read()
        return content
    
def print_file_content(filename):
    with open(filename) as file:
        print(file.read())

def split_string(string, split_char):
    return(string.split(split_char))

def init_1_dim_list(x):
    return([0]*x)

def init_2_dim_list(x, y):
    return([[0]*x for i in range(y)])