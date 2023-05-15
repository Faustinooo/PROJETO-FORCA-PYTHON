palavra = "log"
tentativas = 0
letras_certas = ""
while True:
    tentativas += 1
    letra = str(input("Escolha Uma Letra: "))
    if len(letra) > 1:
        print("DIGITE SOMENTE UMA LETRA")
        continue

    if letra in palavra:
        letras_certas += letra
        tentativas -= 1
    palavra_formada = ""
    for letras in palavra:
        if letras in letras_certas:
            palavra_formada += letras
        else:
            palavra_formada += "*"
    print(palavra_formada)
    if palavra_formada == palavra:
        print("PARABÉNS VOCÊ ACERTOU!")
        if tentativas == 1:
            print(f"\033[31m{tentativas} Erro Foi Registrado\033[m")
        else:
            print(f"\033[31m{tentativas} Erros Foram Registrados\033[m")


        break