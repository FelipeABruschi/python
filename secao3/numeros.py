"""
AJUSTES DE NUMEROS DE PONTO FLUTUANTE
1. formatando string
2. funcao round(numero, casas decimais)
3. usando import decimal
"""

import decimal

n1 = 0.1
n2 = 0.7

n3 = n1 + n2
print(n3)
print(f'{n3:.2f}')
print(round(n3, 3))

nz = decimal.Decimal(0.4)
nx = decimal.Decimal('0.5')
ny = decimal.Decimal('0.4')

print(nz)
print(ny + nx)