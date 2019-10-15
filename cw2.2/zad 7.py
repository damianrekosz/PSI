#lista z zad 6
lista = list(range(1,11))
#print(lista)
lista2 = list()
for i in range(5, 10):
    lista2.append(lista[i])
for j in range(6,11):
    lista.remove(j)
#print(lista)
#print(lista2)

listJoint = list()
for i in lista:
    listJoint.append(i)
for i in lista2:
    listJoint.append(i)
listJoint.insert(0, 0)
listCopy = listJoint
listCopy.sort(reverse=1)

print(listCopy)