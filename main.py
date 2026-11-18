# Main program text for the bookbot assignment.
# Currently must be run in the bookbot dir as paths are relative.

import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    words_in_book = count_words(book)
    #print(f"Found {words_in_book} total words")
    characters_in_book = count_characters(book)
    #print(characters_in_book)
    sorted_characters = sort_characters(characters_in_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_book} total words")
    print("--------- Character Count -------")
    for entry in sorted_characters:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()