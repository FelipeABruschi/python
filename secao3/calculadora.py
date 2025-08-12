while True:
    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operador = input("Digite um operador: (+-*/): ")

    numeros_validos = None

    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("voce digitou algum numero invalido")
        continue

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("operador invalido")
        continue

    if operador == "+":
        print(numero_1_float + numero_2_float)
    elif operador == "-":
        print(numero_1_float - numero_2_float)
    elif operador == "*":
        print(numero_1_float * numero_2_float)
    elif operador == "/":
        print(numero_1_float / numero_2_float)                  

    sair = input("quer sair?").startswith("s")
    
    if sair:
        break