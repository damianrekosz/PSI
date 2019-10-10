lista = list(range(1,11))
print(lista)
lista2 = list()
for i in range(5, 10):
    lista2.append(lista[i])
for j in range(6,11):
    lista.remove(j)
print(lista)
print(lista2)