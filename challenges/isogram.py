def is_isogram(string):
    word = string.lower()
    letter_list = []

    for letter in word:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True


print(is_isogram("helo"))