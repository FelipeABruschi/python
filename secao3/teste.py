letra = 'x'
espaco = ' '
a = 9
b = 1

for i in range(10):
    print(espaco*a + letra*b + letra*(b-1))
    a -= 1
    b += 1