def duplica(numero):
    return numero + numero

def triplica(numero):
    return duplica(numero) + numero

def quadriplica(numero):
    return triplica(numero) + numero

# hkhkhjk
def do_multiplication(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

duplicar = do_multiplication(2)
triplicar = do_multiplication(3)
quadriplicar = do_multiplication(4)

print(duplicar(3))

print(triplicar(4))

print(quadriplicar(5))
