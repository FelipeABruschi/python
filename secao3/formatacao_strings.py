nome = "Felipe"
altura = 1.75
peso = 57
imc = peso / altura ** 2

#F-STRINGS

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

#FORMAT

a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a, b, c)
print(formato)