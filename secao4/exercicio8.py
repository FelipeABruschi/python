lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

lista_soma = list(zip(lista1, lista2))

for i in lista_soma:
    lista_soma[i] = lista_soma[i][i]


print(lista_soma)