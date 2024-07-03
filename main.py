import os

script_dir = os.path.dirname(__file__)
path_to_file = os.path.join(script_dir, 'books/frankenstein.txt')

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    
    char_counts, total_chars = count_characters(file_contents)

    print("---------- Text Analysis Report ----------")
    print(f"File: {path_to_file}")
    print("")

    print("----- Word Count -----")
    print(f"Number of words: {word_count}")
    print("")

    print("----- Character Counts (Ignoring Case and Removing Duplicates) -----")
    for char, count in char_counts.items():
        print(f"{char}: {count}")

    print("")
    print(f"Total number of characters (excluding non-alphabetic): {total_chars}")
    print("-------------------------------------------------")
    

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
    total_chars = sum(char_counts.values())

    return char_counts, total_chars

main()