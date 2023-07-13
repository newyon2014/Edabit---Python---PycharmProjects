def find_letters(word):
    new_list = []
    for c in word:
        if str(word).count(c) == 1:
            new_list.append(c)
    return new_list