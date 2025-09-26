import os
lista = []
x = True

while x:
    print("\nEscolha [i]Inserir - [a]Apagar - [l]Listar - [qualquer tecla]Sair: ")
    teclado = input()

    if teclado == 'i':
        os.system('clear')
        lista.append(input("Digite o item para adicionar na lista: "))
    elif teclado == 'a':
        os.system('clear')
        print("Digite o numero do item para apagar: ")
        num = int(input())
        try:
            lista.pop(num - 1)
        except:
            print("numero nao esta na lista")
    elif teclado == 'l':
        os.system('clear')
        for num, item in enumerate(lista, start=1):
            print(num, item)
    else:
        x = False