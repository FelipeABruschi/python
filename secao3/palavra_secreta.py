palavra = "joao"
tentativas = 0
letras_acertadas = ""
        

while True:
    letra = input("digite uma letra: ")
     
    if len(letra) > 1:
        print("digite apenas 1 letra")
        continue

    tentativas += 1

    if letra in palavra:
        letras_acertadas += letra

    palavra_formada = ""
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print(palavra_formada)

    if palavra_formada == palavra:
        print("voce acertou a palavra")
        print(f"precisou de {tentativas} tentativas")
