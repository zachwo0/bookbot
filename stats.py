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


def get_sorted_chars(char_count):
    sorted_chars = []

    for char, count in char_count.items():
        result = {"char": char, "num": count}
        sorted_chars.append(result)

    sorted_chars.sort(key=lambda d: d["num"], reverse=True)
    return sorted_chars
