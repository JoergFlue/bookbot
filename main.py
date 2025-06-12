import sys

from stats import (
    get_num_words,
    get_character_dictionary,
    chars_dict_to_sorted_list
)
book_path = "books"
book_names = ["frankenstein.txt", ]

def get_book_text(book_name):
    """
    Returns the text of the book with the given name.
    """
    print(f"Reading book: {book_name}")
    return open(book_name).read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    

    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)

    char_dict = get_character_dictionary(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)

    print_report(book_path, num_words, chars_sorted_list)

main()
