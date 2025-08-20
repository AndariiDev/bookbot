from stats import get_num_words
from stats import get_num_chars
from stats import sorted_report

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    file_path = 'books/frankenstein.txt'
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted = sorted_report
    # print(num_words)
    print(f"{num_words} words found in the document")
    print(f"{num_chars} chars found in the document")

if __name__ == '__main__':
    main()
