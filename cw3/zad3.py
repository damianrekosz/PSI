def funkcja(text, letter):
    for char in letter:
        text = text.replace(char, "")
    return text


print(funkcja(text='dsfagdfgaadha', letter='a'))