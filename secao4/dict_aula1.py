time = {
    'nome': 'fallen angels',
    'players': ['top', 'jungle', 'mid', 'adc', 'sup'],
    'regiao': 'LEC'
}

chave = 'pontos'

time[chave] = 4

print(time)

print(time.get('nome', "existe"))