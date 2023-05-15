palavra = "log"  # PALAVRA QUE VAI SER ADVINHADA
tentativas = 0  # NÚMERO DE TENTATIVAS (ACERTOS NÃO SÃO CONTABILIZADOS)
letras_certas = ""  # LETRAS CERTAS DIGITADAS SÃO AUTOMATICAMENTE COLOCADAS AQUI
while True:
    tentativas += 1
    letra = str(input("Escolha Uma Letra: "))  # PERGUNTA UMA LETRA PARA SER DIGITADA
    if len(letra) > 1:  # CASO O USUÁRIO ESCREVA MAIS DE UM CARACTERE É FEITO NOVAMENTE A PERGUNTA
        print("DIGITE SOMENTE UMA LETRA")
        continue

# MÉTODO QUE ADICIONA AS LETRAS CERTAS A "letras_certas" QUE MAIS PREVIAMENTE É IMPRIMIDA
    if letra in palavra:
        letras_certas += letra
        tentativas -= 1
    palavra_formada = ""
    for letras in palavra:
        if letras in letras_certas:
            palavra_formada += letras
        else:
            palavra_formada += "*"
    print(palavra_formada)  # IMPRIME A PALAVRA, "*" É COLOCADO CASO AQUELA LETRA AINDA NÃO TENHA SIDO REVELADA
    if palavra_formada == palavra:
        # CASO O USUÁRIO ACERTE A PALAVRA POR COMPLETO É QUEBRADO ENTÃO O LOOP E O JOGO É FINALIZADO.
        print("PARABÉNS VOCÊ ACERTOU!")
        # VERIFICAÇÃO DO USO DE PLURAL
        if tentativas == 1:
            print(f"\033[31m{tentativas} Erro Foi Registrado\033[m")
        else:
            print(f"\033[31m{tentativas} Erros Foram Registrados\033[m")


        break