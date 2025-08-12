"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 12, 1999, "engenharia", 432, 123]
lista_b = [99, 100]

lista.pop()
print(lista)

lista.pop(3)
print(lista)

lista.append(20)
print(lista)

lista.insert(2, "casa")
print(lista)

del lista[2]
print(lista)

lista.extend(lista_b)
print(lista)