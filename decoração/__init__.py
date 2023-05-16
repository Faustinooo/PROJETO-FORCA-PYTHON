def linha(a = 0):
    print(f"\033[1;{a}m-=\033[m" * 20)

def cabeçalho(a = "TEXTO"):
    print(f"\033[1m{a.center(40)}\033[m")

def texto(a = 0,b = "", c = 32):
    linha(a)
    cabeçalho(f"{b}")
    linha(c)