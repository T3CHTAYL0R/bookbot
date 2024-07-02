import os

script_dir = os.path.dirname(__file__)

path_to_file = os.path.join(script_dir, 'books/frankenstein.txt')

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    print(file_contents)

    word_count = count_words(file_contents)
    print(f"Number of words in the file: {word_count}")

    char_counts, total_chars = count_characters(file_contents)
    print("Character counts (ignoring case and removing duplicates):")
    print(char_counts)
    print(f"Total number of charcters (excluding non-alphabetic): {total_chars}")

def count_words(text):

    words = text.split()

    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    char_counts = {}

    for char in lowered_text:
        if char.isalpha():
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1

    return char_counts

main()