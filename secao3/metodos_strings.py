"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = "olha só que, coisa interessante"

lista = frase.split(',')
lista_frases = []

for i, frase in enumerate(lista):
    lista_frases.append(lista[i].strip())

print(lista_frases)
frases_unidas = ', '.join(lista_frases)

print(frases_unidas)