import sys
from typing import Dict, List

from stats import char_dict_to_sorted_list, get_num_chars, get_num_words, sorted_report


def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    # file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = sorted_report(num_chars)
    sorted_list = char_dict_to_sorted_list(list(num_chars.items()))
    # print(num_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Sorted List ----------")
    print(f"{sorted_list}")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
