numero = input("Digite um numero inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if (numero % 2 == 0):
        print("numero é par")
    else:
        print("numero é impar")
else:
    print("nao eh numero inteiro.")