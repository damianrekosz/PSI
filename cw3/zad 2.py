def textInfo(data_text):
    info = dict()
    info["length"] = len(data_text)
    info["letters"] = list()
    info["bigLetters"] = data_text.upper()
    info["smallLetters"] = data_text.lower()
    for i in data_text:
        info["letters"].append(i)
    return info

text = "Hello World"
print(textInfo(text))