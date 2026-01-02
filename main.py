#main for bookbott
from stats import get_book_words
from stats import get_letters_used

#get text function
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    string_book = get_book_text("books/frankenstein.txt")
    print(f"Found {get_book_words(string_book)} total words")
    letters_used = get_letters_used(string_book)
    print(letters_used)
main()
