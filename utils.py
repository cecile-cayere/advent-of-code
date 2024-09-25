import os

def get_file_content(filename):
    with open(filename) as file:
        content = file.read()
        return content
    
def print_file_content(filename):
    with open(filename) as file:
        print(file.read())