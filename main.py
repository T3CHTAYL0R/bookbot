import os

script_dir = os.path.dirname(__file__)

path_to_file = os.path.join(script_dir, 'books/frankenstein.txt')

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    print(file_contents)

    word_count = count_words(file_contents)
    print(f"Number of words in the file: {word_count}")

def count_words(text):

    words = text.split()

    return len(words)

main()