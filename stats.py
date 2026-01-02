def get_book_words(book_text):
    words_in_book = book_text.split()
    num_words = len(words_in_book) 
    return num_words

def get_letters_used(book_list):
    book_list = book_list.split()
    letters_used = {}
    for word in book_list:
        word = word.lower()
        for ch in word:
            if ch.isalpha():
                letters_used[ch] =letters_used.get(ch, 0) + 1
    return letters_used

