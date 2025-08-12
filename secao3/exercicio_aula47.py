nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not (nome and idade):
    print("Desculpe, voce deixou campos em vazios")
else:
    print("Seu nome é %s" % nome)
    print('Seu nome invertido é %s' % nome[::-1])
    if " " in nome:
        print("seu nome contém espacos")
    else:
        print("seu nome não contem espaços")
    print("seu nome tem %d letras" % len(nome))
    print("a primeira letra do seu nome é %s" % nome[0])
    print("a ultima letra do seu nome é %s" % nome[-1])