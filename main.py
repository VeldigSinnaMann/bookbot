#main for bookbott


#get text function
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def get_book_words(book_text):
    words_in_book = book_text.split()
    num_words = len(words_in_book) 
    return num_words

def main():
    print(f"Found {get_book_words(get_book_text("books/frankenstein.txt"))} total words")
main()
