def multiplicacation(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

produto = multiplicacation(1, 2, 4, 56)

print(produto)

print(1*2*4*56)

def pair(numero):
    if numero % 2 == 0:
        return True
    return False

print(pair(532))
