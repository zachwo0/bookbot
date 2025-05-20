def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_word_count(booktext):
    words_list = booktext.split()
    return len(words_list)


def main():
    book_text = get_book_text('./books/frankenstein.txt')
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")


main()
