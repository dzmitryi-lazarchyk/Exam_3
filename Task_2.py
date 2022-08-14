def check_word(word: str):
    return word == word[::-1]


print(check_word('ololo'))
