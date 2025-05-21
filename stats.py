def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_word_count(booktext):
    words_list = booktext.split()
    return len(words_list)
