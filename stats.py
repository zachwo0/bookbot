def get_word_count(booktext):
    words_list = booktext.split()
    return len(words_list)


def count_characters(booktext):
    characters = {}

    for c in booktext:
        c = c.lower()

        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1

    return characters
