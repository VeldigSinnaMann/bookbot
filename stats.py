def get_book_words(book_text):
    words_in_book = book_text.split()
    num_words = len(words_in_book) 
    return num_words

def get_letters_used(book_list):
    book_list = book_list.lower()
    letters_uesed = {}
    for word in book_list:
        for ch in word:
            if ch.isalpha():
                letters_uesed[ch.lower()] += 1
                

