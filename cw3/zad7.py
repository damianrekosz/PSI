def odwroc(napis):
    odw = list()
    for i in range(len(napis)-1, -1, -1):
        odw.append(napis[i])
    return odw


print(''.join(odwroc("koteł")))
