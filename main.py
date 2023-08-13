from decoração import *
import mod as md
texto(a = 36,b = "FORCA THE GAME",c = 32)
palavra = md.palavra()  # PALAVRA QUE VAI SER ADVINHADA
derrota = f"A Palavra era {palavra}"
tentativas = 0  # NÚMERO DE TENTATIVAS (ACERTOS NÃO SÃO CONTABILIZADOS)
letras_certas = ""  # LETRAS CERTAS DIGITADAS SÃO AUTOMATICAMENTE COLOCADAS AQUI
letras_erradas = "" # LETRAS ERRADAS SÃO COLOCADAS AQUI
while True:
    tentativas += 1
    letra = str(input("Escolha Uma Letra: ").strip().upper())  # PERGUNTA UMA LETRA PARA SER DIGITADA
    if len(letra) > 1 or letra.isdigit() or letra == "":  # CASO O USUÁRIO ESCREVA MAIS DE UM CARACTERE É FEITO NOVAMENTE A PERGUNTA
        print("\033[31mDIGITAÇÃO INCORRETA\033[m")
        tentativas -= 1
        continue
    if letra in letras_erradas:
        print(f"\033[31mA LETRA ({letra}) JA FOI DIGITADA\033[m")
        tentativas -= 1
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
            letras_erradas += letra
            palavra_formada += "_"
    print(palavra_formada)  # IMPRIME A PALAVRA, "*" É COLOCADO CASO AQUELA LETRA AINDA NÃO TENHA SIDO REVELADA
    if tentativas == 0:
        print(''' |------|
        |
        |
        |''')
    elif tentativas == 1:
        print(''' |------|
 O      |
        |
        |''')
    elif tentativas == 2:
        print(''' |------|
 O      |
/       |
        |''')
    elif tentativas == 2:
        print(''' |------|
 O      |
/|      |
        |''')
    elif tentativas == 4:
        print(''' |------|
  O     |
 /|\    |
        |''')
    elif tentativas == 5:
        print(''' |------|
 O      |
/|\     |
/       |''')
    elif tentativas == 6:
        print(''' |------|
 O      |
/|\     |
/ \     |''')
        texto(31,"NÃO FOI DESSA VEZ",31)
        print(f"\033[31m{derrota.center(40)}\033[m")
        break
    if palavra_formada == palavra:
        # CASO O USUÁRIO ACERTE A PALAVRA POR COMPLETO É QUEBRADO ENTÃO O LOOP E O JOGO É FINALIZADO.
        texto(32,"PARABÉNS VOCÊ ACERTOU")
        # VERIFICAÇÃO DO USO DE PLURAL
        if tentativas == 1:
            print(f"\033[31m{tentativas} Erro Foi Registrado\033[m")
        else:
            print(f"\033[31m{tentativas} Erros Foram Registrados\033[m")


        break
