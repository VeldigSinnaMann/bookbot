#main for bookbott
from stats import get_book_words
from stats import get_letters_used

#get text function
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    print(f"Found {get_book_words(get_book_text("books/frankenstein.txt"))} total words")
main()
