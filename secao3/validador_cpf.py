cpf = "249.848.020-06"

divide_cpf = cpf.split('-')
p1, p2 = divide_cpf

aux1, aux2 = p2
digito1 = int(aux1)
digito2 = int(aux2)

soma1 = 0
m = 10

for i in p1:
    if i == '.':
        continue
    else:
        soma1 += m * int(i)
        m = m-1

d1 = soma1 * 10
d1 = d1 % 11

d1 = d1 if d1 < 10 else 0

soma2 = 0
m = 11

for i in p1:
    if i == '.':
        continue
    else:
        soma2 += m * int(i)
        m -= 1

soma2 += d1 * 2
d2 = soma2 * 10 % 11

d2 = d2 if d2 < 10 else 0

if d1 == digito1 and d2 == digito2:
    print(d1)
    print(d2)
    print("cpf válido")
else:
    print("cpf inválido")