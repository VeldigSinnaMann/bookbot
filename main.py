#main for bookbott
import sys
from stats import get_book_words
from stats import get_letters_used
from stats import sort_on
from stats import sort_dictionaries
from stats import print_report
#get text function
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        string_book = get_book_text(file_path)
        word_count = get_book_words(string_book)
        letters_used = get_letters_used(string_book)
        sorted_ch = sort_dictionaries(letters_used)
        print_report(file_path, word_count, sorted_ch)
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
