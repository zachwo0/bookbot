from stats import get_word_count, count_characters


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text('./books/frankenstein.txt')
    word_count = get_word_count(book_text)
    character_count = count_characters(book_text)
    print(f"{word_count} words found in the document")
    print(character_count)


main()
