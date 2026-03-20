# 26. Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

# Declarar 
v1: int = 0
v2: int = 0

# Inicio
v1 = int(input("Informe o valor 1: "))
v2 = int(input("Informe o valor 2: "))

if v1 == v2:
    print("Valores iguais!")
elif v1 > v2:
    if v1 % v2 == 0:
        print("É multiplo!")
    else:
        print("Não é multiplo")
else:
    if v2 % v1 == 0:
        print("É multiplo!")
    else:
        print("Não é multiplo")
# Fim