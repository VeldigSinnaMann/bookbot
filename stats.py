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

def sort_on(item):
    return item["num"]


def sort_dictionaries(dictionary):
    character_count = [] 
    for char, number in dictionary.items():
        character_count.append({"char": char, "num": number})
    character_count.sort(reverse=True , key=sort_on)
    return character_count


def print_report(filepath, wordcount, sorted_ch):
    print(
          "============ BOOKBOT ============\n"
          f"Analyzing book found at {filepath}...\n"
          "----------- Word Count ----------\n"
          f"Found {wordcount} total words\n"
          "--------- Character Count -------"
          )
    for ch in sorted_ch:
        print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")