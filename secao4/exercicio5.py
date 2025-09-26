import copy

produtos = [
    {'nome': "produto 5", 'preco': 10.00},
    {'nome': "produto 1", 'preco': 22.32},
    {'nome': "produto 3", 'preco': 10.11},
    {'nome': "produto 2", 'preco': 105.87},
    {'nome': "produto 4", 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)


for produto in novos_produtos:
    produto['preco'] *= 1.1
    print(produto['nome'], f'{produto['preco']:.2f}')

novos_produtos.sort(key=lambda item: item['nome'], reverse=True)
print(*novos_produtos, sep='\n')

novos_produtos.sort(key=lambda item: item['preco'])
print(*novos_produtos, sep='\n')