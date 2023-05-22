def alpha_position(text):
    text = text.lower()
    string = ""
    for i in text:
        if i.isalpha():
            string += str(ord(i)-96)
            string += " "
    return string.rstrip()
