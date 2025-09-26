conjunto = set()
colecao = {2, 4, 6, 6, 1, 2, 5, 1, "felipe"}

print(conjunto)
print(colecao, type(colecao))

conjunto.add(5)

print(conjunto)

colecao.clear

conjunto.discard(5)

conjunto.update((44, 34, 12))


print(conjunto)