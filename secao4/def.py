def soma(a, b):
    return a + b
def multiplicacao(a, b):
    return a * b
def div(a, b):
    return a / b

x = soma(3, 4)
y = multiplicacao(3, 4)
z = div(3, 4)

print(x)
print(y)
print(z)

def saudacao(nome="sem nome"):
    print(f'Olá {nome}')

saudacao("felipe")
saudacao()