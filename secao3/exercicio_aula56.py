horario = input("digite o horario: ")

if horario.isdigit:
    horario = int(horario)
    if horario <= 11:
        print("bom dia")
    elif horario < 18:
        print("boa tarde")
    else:
        print("boa noite")
else:
    print("hora invalida")

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')