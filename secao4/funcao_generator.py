def generator(n=0):
    yield 0
    print("continuando")
    yield 1
    print("mais uma")
    yield 2
    print("omg")
    return "acabou"


gen = generator()

print(gen)

print(next(gen))
print(next(gen))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)