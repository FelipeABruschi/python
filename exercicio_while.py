nome = "felipe augusto"

newstr = ""

tamanho_nome = len(nome)

contador = 0

while contador < tamanho_nome:
    newstr += f"*{nome[contador]}"
    contador += 1

newstr += '*'
print(newstr)