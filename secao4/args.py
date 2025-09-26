# args recebe quantos argumentos quiser e os transforma em uma tupla


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

x = soma(2, 544, 1, 100, 40)

a = 10, 20, 30

print(sum(a, 5))