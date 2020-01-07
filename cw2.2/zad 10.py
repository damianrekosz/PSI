import random
telList = []
s = set()

for i in range(10):
    telList.append(random.randrange(567890,567899))
print (telList)

for i in telList:
    s.add(i)

print (s)