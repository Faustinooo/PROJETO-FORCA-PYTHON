def linha(a = 31):
    print(f"\033[1;{a}m-=\033[m" * 20 )

def cabeçalho(a = "TEXTO"):
    print(f"\033[1m{a.center(40)}\033[m")

def texto(a = 36,b = "", c = 32):
    linha(36)
    cabeçalho(f"{b}")
    linha(32)