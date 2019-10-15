import random

dict1 = dict()
dict2 = dict()
dict3 = dict()
dictList = []
final = ''

for i in range(random.randrange(10)+1):
    dict1[i] = i * random.randrange(10)
for i in range(random.randrange(10)+1):
    dict2[i] = "jakiś string nr " + (i+1).__str__()
for i in range(random.randrange(10)+1):
    dict3[i] = i * random.randrange(10)

print(dict1)
print(dict2)
print(dict3)

for i in range(max(len(dict1.keys()), len(dict2.keys()), len(dict3.keys()))):
    if (i in dict1.keys()):
        final += "z pierwszego słownika: " + dict1[i].__str__() + ', '
    if (i in dict2.keys()):
        final += "z drugiego słownika: " + dict2[i].__str__() + ', '
    if (i in dict3.keys()):
        final += "z trzeciego słownika: " + dict3[i].__str__() + '; '

print(final)