from stats import get_word_count, count_characters, get_sorted_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = './books/frankenstein.txt'
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    character_count = count_characters(book_text)
    sorted_chars = get_sorted_chars(character_count)
    print(f"""
          ============ BOOKBOT ============
          Analyzing book found at {filepath}
          ----------- Word Count ----------
          Found {word_count} total words
          --------- Character Count -------
    """)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
