perguntas = [
    {
        'pergunta': 'quanto é 2 + 2?',
        'opcoes': [2, 4, 22, 10],
        'resposta': 4,
    },
    {
        'pergunta': 'quanto é 5 * 5?',
        'opcoes': [5, 10, 25, 1],
        'resposta': 25,
    },
    {
        'pergunta': 'quanto é 10 / 2?',
        'opcoes': [5, 8, 12, 2],
        'resposta': 5,
    },
]

acertos = 0
for dicionario in perguntas:
    chaves = list(dicionario.keys())
    valores = list(dicionario.values())
    while True:
        print(f'{chaves[0]}: {valores[0]}')
        for i, opcoes in enumerate(valores[1]):
            print(f'{i}) {opcoes}')
        try:
            entrada = int(input("Escolha uma opcao: "))
            if valores[1][entrada] == valores[2]:
                print("Acertou!")
                acertos += 1
            else:
                print("Errou!")
            break
        except(ValueError, IndexError):
            print("Escolha uma opcao entre 0 e 3.")
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')