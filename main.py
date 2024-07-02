import os

script_dir = os.path.dirname(__file__)

path_to_file = os.path.join(script_dir, 'books/frankenstein.txt')

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    print(file_contents)

main()