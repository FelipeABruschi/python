# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.

# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo)
    ]

cidades = ['Salvador', 'Campinas', 'Belo horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cidades, estados)))