lista = []
x = True

while x:
    print("\nEscolha [i]Inserir - [a]Apagar - [l]Listar - [qualquer tecla]Sair: ")
    teclado = input()

    if teclado == 'i':
        lista.append(input("Digite o item para adicionar na lista: "))
    elif teclado == 'a':
        print("Digite o numero do item para apagar: ")
        num = int(input())
        try:
            lista.pop(num - 1)
        except:
            print("numero nao esta na lista")
    elif teclado == 'l':
        for num, item in enumerate(lista, start=1):
            print(num, item)
    else:
        x = False